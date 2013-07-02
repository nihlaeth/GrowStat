from pyramid.view import view_config
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.httpexceptions import HTTPFound
import shutil
import imghdr
import os
#import helpers as h

import logging
log = logging.getLogger(__name__)

here = os.path.dirname(os.path.abspath(__file__))
TIMES = [
        "0000", "0030", "0100", "0130", "0200", "0230",
        "0300", "0330", "0400", "0430", "0500", "0530",
        "0600", "0630", "0700", "0730", "0800", "0830",
        "0900", "0930", "1000", "1030", "1100", "1130",
        "1200", "1230", "1300", "1330", "1400", "1430",
        "1500", "1530", "1600", "1630", "1700", "1730",
        "1800", "1830", "1900", "1930", "2000", "2030",
        "2100", "2130", "2200", "2230", "2300", "2330"]

TIMES_T = ['t' + time for time in TIMES]

@view_config(route_name='home', renderer='home.mako')
def home_view(request):
    cursor=request.db.cursor()
    cursor.execute('select sum(weight) from harvest')
    totalharvest=cursor.fetchone()[0]/1000
    #this one is complicated, can't just add everything up and plants get shorter after harvest sometimes
    cursor.execute('select * from height order by tstamp asc')
    heights=cursor.fetchall()
    totalgrowth=0
    growth={}
    for record in heights:
        last=growth.get(str(record[2]),{}).get('last',0)
        g=growth.get(str(record[2]),{}).get('growth',0)
        diff=float(record[3])-last
        try:
            growth[str(record[2])]['last']=record[3]
        except KeyError:
            growth[str(record[2])]={}
            growth[str(record[2])]['last']=record[3]
        if diff>=0:
            #plant has grown, not shrunken
            growth[str(record[2])]['growth']=g+diff
    for plant in growth:
        totalgrowth+=growth[str(plant)]['growth']
    totalgrowth=totalgrowth/100
    cursor.execute('select * from plants where slot!=0')
    totalliveplants=cursor.fetchone()[0]
    cursor.execute('select avg(ph) from ph')
    averageph=cursor.fetchone()[0]
    cursor.execute('select avg(ec) from ec')
    averageec=cursor.fetchone()[0]
    cursor.execute('select avg(temp) from temp')
    averagetemp=cursor.fetchone()[0]
    cursor.execute('select avg(humidity) from humidity')
    averagehumidity=cursor.fetchone()[0]
    return {'totalharvest': totalharvest, 'totalgrowth': totalgrowth, 'totalliveplants': totalliveplants, \
    'averageph': averageph, 'averageec': averageec, 'averagetemp': averagetemp, 'averagehum': averagehumidity}

@view_config(route_name='addsupply', renderer='addsupply.mako')
def addsupply_view(request):
    if not request.method =='POST':
        pass
    elif not request.POST['name']:
        request.session.flash('You have to fill out a name!')
    else:
        request.db.execute('insert into supplies (name) values ( ? )',[request.POST['name']])
        request.db.commit()
        request.session.flash('Water supply added successfully!')
        return HTTPFound(location=request.route_url('list'))
    return {}

@view_config(route_name='addplant', renderer='addplant.mako')
def addplant_view(request):
    if not request.method =='POST':
        pass
    elif not request.POST['name'] or not request.POST['slot'] or not request.POST['lname']:
        request.session.flash('You have to fill out a name, latin name and a slot!')
    else:
        cur=request.db.cursor()
        cur.execute('select count(*) from slots where id = ?', [request.POST['slot']])
        count=cur.fetchone()[0]
        if count != 1:
            request.session.flash('That is not a valid slot!')
        else:
            request.db.execute('insert into plants (name, lname, slot) values ( ?, ?, ? )',[request.POST['name'], request.POST['lname'], request.POST['slot']])
            request.db.commit()
            request.session.flash('Plant added successfully!')
            return HTTPFound(location=request.route_url('list'))
    cursor=request.db.cursor()
    cursor.execute('select * from slots where id != ?', [0])
    slots=cursor.fetchall()
    cursor.execute('select * from columns where id!=0')
    cols=cursor.fetchall()
    cursor.execute('select * from supplies where id!=0')
    supplies=cursor.fetchall()
    cursor.execute('select * from plants where slot!=0')
    plants=cursor.fetchall()
    return {'slots' : slots, 'columns' : cols, 'supplies': supplies, 'plants' : plants}

@view_config(route_name='addslot', renderer='addslot.mako')
def addslot_view(request):
    if not request.method =='POST':
        pass
    elif not request.POST['name'] or not request.POST['column']:
        request.session.flash('You have to fill out a name and a column!')
    else:
        cur=request.db.cursor()
        cur.execute('select count(*) from columns where id = ?', [request.POST['column']])
        count=cur.fetchone()[0]
        if count != 1:
            request.session.flash('That is not a valid column!')
        else:
            request.db.execute('insert into slots (name, col) values ( ?, ? )',[request.POST['name'], request.POST['column']])
            request.db.commit()
            request.session.flash('Slot added successfully!')
            return HTTPFound(location=request.route_url('list'))
    cursor=request.db.cursor()
    cursor.execute('select * from columns where id != ?', [0])
    columns=cursor.fetchall()
    cursor.execute('select * from supplies where id!=0')
    supplies=cursor.fetchall()
    return {'columns' : columns, 'supplies':supplies}

@view_config(route_name='addcolumn', renderer='addcolumn.mako')
def addcolumn_view(request):
    if not request.method =='POST':
        pass
    elif not request.POST['name'] or not request.POST['supply']:
        request.session.flash('You have to fill out a name and a water supply!')
    else:
        cur=request.db.cursor()
        cur.execute('select count(*) from supplies where id = ?', [request.POST['supply']])
        count=cur.fetchone()[0]
        if count != 1:
            request.session.flash('That is not a valid water supply!')
        else:
            request.db.execute('insert into columns (name, supply) values ( ?, ? )',[request.POST['name'], request.POST['supply']])
            request.db.commit()
            request.session.flash('Column added successfully!')
            return HTTPFound(location=request.route_url('list'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    return {'supplies' : supplies}

@view_config(route_name='ph', renderer='ph.mako')
def ph_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['ph'] or not request.POST['supply']:
        request.session.flash('Both ph and water supply have to be filled out!')
    elif not isinstance(float(request.POST['ph']),float):
        request.session.flash('PH must be numerical!')
    elif not isinstance(int(request.POST['supply']),int):
        request.session.flash('This is not a valid water supply!')
    else :
        #now check if the supply exists
        supply=int(request.POST['supply'])
        ph=float(request.POST['ph'])
        cur=request.db.cursor()
        cur.execute('select count(*) from supplies where id = ?', [supply])
        count=cur.fetchone()[0]
        if count !=1 :
            request.session.flash('This water supply does not exist!')
        else:
            request.db.execute('insert into ph (ph, supply) values (?, ?)', [ph, supply])
            request.db.commit()
            request.session.flash('PH value was recorded successfully!')
            return HTTPFound(location=request.route_url('home'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    #    request.db.execute('select * from supplies where id != 0')
    #    supplies=request.db.fetchall()
    supplies=cursor.fetchall()
    #    request.session.flash('Flash still works!')
    return {'supplies' : supplies}

@view_config(route_name='ec', renderer='ec.mako')
def ec_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['ec'] or not request.POST['supply']:
        request.session.flash('Both ec and water supply have to be filled out!')
    elif not isinstance(float(request.POST['ec']),float):
        request.session.flash('EC must be numerical!')
    elif not isinstance(int(request.POST['supply']),int):
        request.session.flash('This is not a valid water supply!')
    else :
        #now check if the supply exists
        supply=int(request.POST['supply'])
        ec=float(request.POST['ec'])
        cur=request.db.cursor()
        cur.execute('select count(*) from supplies where id = ?', [supply])
        count=cur.fetchone()[0]
        if count !=1 :
            request.session.flash('This water supply does not exist!')
        else:
            request.db.execute('insert into ec (ec, supply) values (?, ?)', [ec, supply])
            request.db.commit()
            request.session.flash('EC value was recorded successfully!')
            return HTTPFound(location=request.route_url('home'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    return {'supplies' : supplies}

@view_config(route_name='water', renderer='water.mako')
def water_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['water'] or not request.POST['supply']:
        request.session.flash('Both water and water supply have to be filled out!')
    elif not isinstance(float(request.POST['water']),float):
        request.session.flash('water must be numerical!')
    elif not isinstance(int(request.POST['supply']),int):
        request.session.flash('This is not a valid water supply!')
    else :
        #now check if the supply exists
        supply=int(request.POST['supply'])
        water=float(request.POST['water'])
        cur=request.db.cursor()
        cur.execute('select count(*) from supplies where id = ?', [supply])
        count=cur.fetchone()[0]
        if count !=1 :
            request.session.flash('This water supply does not exist!')
        else:
            request.db.execute('insert into water (volume, supply) values (?, ?)', [water, supply])
            request.db.commit()
            request.session.flash('Water value was recorded successfully!')
            return HTTPFound(location=request.route_url('home'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    return {'supplies' : supplies}

@view_config(route_name='temp', renderer='temp.mako')
def temp_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['temp'] or not request.POST['supply']:
        request.session.flash('Both temperature and water supply have to be filled out!')
    elif not isinstance(float(request.POST['temp']),float):
        request.session.flash('Temperature must be numerical!')
    elif not isinstance(int(request.POST['supply']),int):
        request.session.flash('This is not a valid water supply!')
    else :
        #now check if the supply exists
        supply=int(request.POST['supply'])
        temp=float(request.POST['temp'])
        cur=request.db.cursor()
        cur.execute('select count(*) from supplies where id = ?', [supply])
        count=cur.fetchone()[0]
        if count !=1 :
            request.session.flash('This water supply does not exist!')
        else:
            request.db.execute('insert into temp (temp, supply) values (?, ?)', [temp, supply])
            request.db.commit()
            request.session.flash('Temperature value was recorded successfully!')
            return HTTPFound(location=request.route_url('home'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    return {'supplies' : supplies}

@view_config(route_name='humidity', renderer='humidity.mako')
def humidity_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['humidity']:
        request.session.flash('Humidity has to be filled out!')
    elif not isinstance(float(request.POST['humidity']),float):
        request.session.flash('humidity must be numerical!')
    else :
        request.db.execute('insert into humidity (humidity) values (?)', [request.POST['humidity']])
        request.db.commit()
        request.session.flash('Humidity was recorded successfully!')
        return HTTPFound(location=request.route_url('home'))
    return {}

@view_config(route_name='nutrients', renderer='nutrients.mako')
def nutrients_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['name'] or not request.POST['supply'] or not request.POST['amount'] or not request.POST['unit']:
        request.session.flash('All fields have to be filled out!')
    elif not isinstance(int(request.POST['supply']),int):
        request.session.flash('This is not a valid water supply!')
    elif not isinstance(float(request.POST['amount']),float):
        request.session.flash('This is not a valid amount!')
    else :
        #now check if the supply exists
        supply=int(request.POST['supply'])
        name=request.POST['name']
        amount=request.POST['amount']
        unit=request.POST['unit']
        cur=request.db.cursor()
        cur.execute('select count(*) from supplies where id = ?', [supply])
        count=cur.fetchone()[0]
        if count !=1 :
            request.session.flash('This water supply does not exist!')
        else:
            request.db.execute('insert into nutrients (name, amount, unit, supply) values (?, ?, ?, ?)', [name, amount, unit, supply])
            request.db.commit()
            request.session.flash('Nutrients were recorded successfully!')
            return HTTPFound(location=request.route_url('home'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    return {'supplies' : supplies}

@view_config(route_name='height', renderer='height.mako')
def height_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['height'] or not request.POST['plant']:
        request.session.flash('Both height and plant to be filled out!')
    elif not isinstance(float(request.POST['height']),float):
        request.session.flash('Height must be numerical!')
    elif not isinstance(int(request.POST['plant']),int):
        request.session.flash('This is not a valid plant!')
    else :
        #now check if the plant exists
        plant=int(request.POST['plant'])
        height=float(request.POST['height'])
        cur=request.db.cursor()
        cur.execute('select count(*) from plants where id = ?', [plant])
        count=cur.fetchone()[0]
        if count !=1 :
            request.session.flash('This plant does not exist!')
        else:
            request.db.execute('insert into height (height, plant) values (?, ?)', [height, plant])
            request.db.commit()
            request.session.flash('Plant height was recorded successfully!')
            return HTTPFound(location=request.route_url('home'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    cursor.execute('select * from columns where id !=?', [0])
    columns=cursor.fetchall()
    cursor.execute('select * from slots where id !=?', [0])
    slots=cursor.fetchall()
    cursor.execute('select * from plants where slot!=?',[0])
    plants=cursor.fetchall()
    return {'supplies' : supplies, 'columns' : columns, 'slots' : slots, 'plants' : plants}

# Helper function to produce SQL statement for use of watering view
# (Nihlaeth's old code, split into separate function)
def make_watering_sql_old(ID):
    sql = 'update timerconfigs set '

    sql2 = 'insert into chtc (tcid,t0000,t0030,t0100,t0130,t0200,t0230,t0300,t0330,'
    sql2+='t0400,t0430,t0500,t0530,t0600,t0630,t0700,t0730,t0800,t0830,t0900,t0930,'
    sql2+='t1000,t1030,t1100,t1130,t1200,t1230,t1300,t1330,t1400,t1430,t1500,t1530,'
    sql2+='t1600,t1630,t1700,t1730,t1800,t1830,t1900,t1930,t2000,t2030,t2100,t2130,'
    sql2+='t2200,t2230,t2300,t2330) values (' + ID + ','
    
    if request.POST.get('t0000', 0)=='1': 
        sql+= 't0000=1, '; sql2+= '1,'
    else : 
        sql+= 't0000=0, '; sql2+= '0,'
    if request.POST.get('t0030', 0)=='1': sql+= 't0030=1, '; sql2+= '1,'
    else : sql+= 't0030=0, '; sql2+= '0,'
    if request.POST.get('t0100', 0)=='1': sql+= 't0100=1, '; sql2+= '1,'
    else : sql+= 't0100=0, '; sql2+= '0,'
    if request.POST.get('t0130', 0)=='1': sql+= 't0130=1, '; sql2+= '1,'
    else : sql+= 't0130=0, '; sql2+= '0,'
    if request.POST.get('t0200', 0)=='1': sql+= 't0200=1, '; sql2+= '1,'
    else : sql+= 't0200=0, '; sql2+= '0,'
    if request.POST.get('t0230', 0)=='1': sql+= 't0230=1, '; sql2+= '1,'
    else : sql+= 't0230=0, '; sql2+= '0,'
    if request.POST.get('t0300', 0)=='1': sql+= 't0300=1, '; sql2+= '1,'
    else : sql+= 't0300=0, '; sql2+= '0,'
    if request.POST.get('t0330', 0)=='1': sql+= 't0330=1, '; sql2+= '1,'
    else : sql+= 't0330=0, '; sql2+= '0,'
    if request.POST.get('t0400', 0)=='1': sql+= 't0400=1, '; sql2+= '1,'
    else : sql+= 't0400=0, '; sql2+= '0,'
    if request.POST.get('t0430', 0)=='1': sql+= 't0430=1, '; sql2+= '1,'
    else : sql+= 't0430=0, '; sql2+= '0,'
    if request.POST.get('t0500', 0)=='1': sql+= 't0500=1, '; sql2+= '1,'
    else : sql+= 't0500=0, '; sql2+= '0,'
    if request.POST.get('t0530', 0)=='1': sql+= 't0530=1, '; sql2+= '1,'
    else : sql+= 't0530=0, '; sql2+= '0,'
    if request.POST.get('t0600', 0)=='1': sql+= 't0600=1, '; sql2+= '1,'
    else : sql+= 't0600=0, '; sql2+= '0,'
    if request.POST.get('t0630', 0)=='1': sql+= 't0630=1, '; sql2+= '1,'
    else : sql+= 't0630=0, '; sql2+= '0,'
    if request.POST.get('t0700', 0)=='1': sql+= 't0700=1, '; sql2+= '1,'
    else : sql+= 't0700=0, '; sql2+= '0,'
    if request.POST.get('t0730', 0)=='1': sql+= 't0730=1, '; sql2+= '1,'
    else : sql+= 't0730=0, '; sql2+= '0,'
    if request.POST.get('t0800', 0)=='1': sql+= 't0800=1, '; sql2+= '1,'
    else : sql+= 't0800=0, '; sql2+= '0,'
    if request.POST.get('t0830', 0)=='1': sql+= 't0830=1, '; sql2+= '1,'
    else : sql+= 't0830=0, '; sql2+= '0,'
    if request.POST.get('t0900', 0)=='1': sql+= 't0900=1, '; sql2+= '1,'
    else : sql+= 't0900=0, '; sql2+= '0,'
    if request.POST.get('t0930', 0)=='1': sql+= 't0930=1, '; sql2+= '1,'
    else : sql+= 't0930=0, '; sql2+= '0,'
    if request.POST.get('t1000', 0)=='1': sql+= 't1000=1, '; sql2+= '1,'
    else : sql+= 't1000=0, '; sql2+= '0,'
    if request.POST.get('t1030', 0)=='1': sql+= 't1030=1, '; sql2+= '1,'
    else : sql+= 't1030=0, '; sql2+= '0,'
    if request.POST.get('t1100', 0)=='1': sql+= 't1100=1, '; sql2+= '1,'
    else : sql+= 't1100=0, '; sql2+= '0,'
    if request.POST.get('t1130', 0)=='1': sql+= 't1130=1, '; sql2+= '1,'
    else : sql+= 't1130=0, '; sql2+= '0,'
    if request.POST.get('t1200', 0)=='1': sql+= 't1200=1, '; sql2+= '1,'
    else : sql+= 't1200=0, '; sql2+= '0,'
    if request.POST.get('t1230', 0)=='1': sql+= 't1230=1, '; sql2+= '1,'
    else : sql+= 't1230=0, '; sql2+= '0,'
    if request.POST.get('t1300', 0)=='1': sql+= 't1300=1, '; sql2+= '1,'
    else : sql+= 't1300=0, '; sql2+= '0,'
    if request.POST.get('t1330', 0)=='1': sql+= 't1330=1, '; sql2+= '1,'
    else : sql+= 't1330=0, '; sql2+= '0,'
    if request.POST.get('t1400', 0)=='1': sql+= 't1400=1, '; sql2+= '1,'
    else : sql+= 't1400=0, '; sql2+= '0,'
    if request.POST.get('t1430', 0)=='1': sql+= 't1430=1, '; sql2+= '1,'
    else : sql+= 't1430=0, '; sql2+= '0,'
    if request.POST.get('t1500', 0)=='1': sql+= 't1500=1, '; sql2+= '1,'
    else : sql+= 't1500=0, '; sql2+= '0,'
    if request.POST.get('t1530', 0)=='1': sql+= 't1530=1, '; sql2+= '1,'
    else : sql+= 't1530=0, '; sql2+= '0,'
    if request.POST.get('t1600', 0)=='1': sql+= 't1600=1, '; sql2+= '1,'
    else : sql+= 't1600=0, '; sql2+= '0,'
    if request.POST.get('t1630', 0)=='1': sql+= 't1630=1, '; sql2+= '1,'
    else : sql+= 't1630=0, '; sql2+= '0,'
    if request.POST.get('t1700', 0)=='1': sql+= 't1700=1, '; sql2+= '1,'
    else : sql+= 't1700=0, '; sql2+= '0,'
    if request.POST.get('t1730', 0)=='1': sql+= 't1730=1, '; sql2+= '1,'
    else : sql+= 't1730=0, '; sql2+= '0,'
    if request.POST.get('t1800', 0)=='1': sql+= 't1800=1, '; sql2+= '1,'
    else : sql+= 't1800=0, '; sql2+= '0,'
    if request.POST.get('t1830', 0)=='1': sql+= 't1830=1, '; sql2+= '1,'
    else : sql+= 't1830=0, '; sql2+= '0,'
    if request.POST.get('t1900', 0)=='1': sql+= 't1900=1, '; sql2+= '1,'
    else : sql+= 't1900=0, '; sql2+= '0,'
    if request.POST.get('t1930', 0)=='1': sql+= 't1930=1, '; sql2+= '1,'
    else : sql+= 't1930=0, '; sql2+= '0,'
    if request.POST.get('t2000', 0)=='1': sql+= 't2000=1, '; sql2+= '1,'
    else : sql+= 't2000=0, '; sql2+= '0,'
    if request.POST.get('t2030', 0)=='1': sql+= 't2030=1, '; sql2+= '1,'
    else : sql+= 't2030=0, '; sql2+= '0,'
    if request.POST.get('t2100', 0)=='1': sql+= 't2100=1, '; sql2+= '1,'
    else : sql+= 't2100=0, '; sql2+= '0,'
    if request.POST.get('t2130', 0)=='1': sql+= 't2130=1, '; sql2+= '1,'
    else : sql+= 't2130=0, '; sql2+= '0,'
    if request.POST.get('t2200', 0)=='1': sql+= 't2200=1, '; sql2+= '1,'
    else : sql+= 't2200=0, '; sql2+= '0,'
    if request.POST.get('t2230', 0)=='1': sql+= 't2230=1, '; sql2+= '1,'
    else : sql+= 't2230=0, '; sql2+= '0,'
    if request.POST.get('t2300', 0)=='1': sql+= 't2300=1, '; sql2+= '1,'
    else : sql+= 't2300=0, '; sql2+= '0,'
    if request.POST.get('t2330', 0)=='1': sql+= 't2330=1 '; sql2+= '1'
    else : sql+= 't2330=0 '; sql2+= '0'
    sql += 'where id=' + ID
    sql2 +=')'
    return sql, sql2

# Helper function to produce SQL statement for use of watering view
# (Sietse's refactoring)
def make_watering_sql_new(ID)
    # First collect the bits and bobs of the SQL statements
    # Initialize lists, then grow them. (Using map() would work, too,
    # except python doesn't support two-line lambdas.)
    values = []       # collection of [1, 0, ...]
    assignments = []  # collection of ['t0000=1', 't0030=0', ...]
    for time_i in TIMES_T:
        val = int(request.POST.get(time_i, 0) == 1)
        values.append(val)
        assignments.append('{0}={1}'.format(time_i, val))
    
    # Next, create the SQL statements
    sql = ('update timerconfigs set {assignments} where id={ID}').format(
            assignments = assignments, 
            ID = ID)
    # Implicit string continuation is brilliant: consecutive string
    # literals in one statement (no comma in between!) get concatenated
    # automatically.
    # str.format is excellent, too.
    sql = ('insert ' 
           'into chtc (tcid, {times}) '
           'values ({ID}, {values})').format(
                   times = ", ".join(TIMES_T),
                   ID = ID,
                   values = values)
    return sql, sql2

@view_config(route_name='watering', renderer='watering.mako')
def watering_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['action']:
        request.session.flash('Cross site scripting is not allowed!')
    elif request.POST['action']=="add":
        if not request.POST['name']:
            request.session.flash('You must fill out a name!')
        else:
            request.db.execute('insert into timerconfigs (name) values (?)', [request.POST['name']])
            request.db.commit() #I'm not sure last_insert_rowid is updated before a commit, so just to be on the safe side here
            request.db.execute('insert into chtc (tcid) values(last_insert_rowid())')
            request.db.commit()
            request.session.flash('Successfully created new timer setting!')
            return HTTPFound(location=request.route_url('watering'))
    elif request.POST['action']=="edit":
        try:
            #do your thing
            if not isinstance(int(request.POST['id']),int):
                request.session.flash('This is not valid input!')
            else:
                # Create the SQL statements (code factored out)
                # FIXME what type is request.POST['id']? 
                # str(int(...)) seems redundant.
                ID = str(int(request.POST['id']))
                sql, sql2 = make_watering_sql_new(ID)
                sqlo, sql2o = make_watering_sql_old(ID)
                # TODO test whether sql == sqlo before switching to
                # refactored version.

                request.db.execute(sql)
                request.db.execute(sql2)
                request.db.commit()
                request.session.flash('TimerConfig saved!')
                return HTTPFound(location=request.route_url('watering'))
        except KeyError:
            request.session.flash('You have to fill out everything') 
    elif request.POST['action']=="assign":
        if not isinstance(int(request.POST['supply']),int) or not isinstance(int(request.POST['timerconfig']),int):
            request.session.flash('This is not a valid input!')
        else :
            #now check if the supply exists
            supply=int(request.POST['supply'])
            timerconfig=float(request.POST['timerconfig'])
            cur=request.db.cursor()
            cur.execute('select count(*) from supplies where id = ?', [supply])
            count=cur.fetchone()[0]
            cur.execute('select count(*) from timerconfigs where id = ?', [timerconfig])
            count2=cur.fetchone()[0]
            if count !=1 or count2!=1:
                request.session.flash('Either the timer config or the water supply does not exist!')
            else:
                request.db.execute('insert into watering (timerconfig, supply) values (?, ?)', [timerconfig, supply])
                request.db.commit()
                request.session.flash('Watering setting was recorded successfully!')
                return HTTPFound(location=request.route_url('home'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    cursor.execute('select * from timerconfigs')
    timerconfigs=cursor.fetchall()
    cursor.execute('select * from watering')
    watering=cursor.fetchall()
    water={}
    for w in watering:
        if water.get(str(w[2]),{}).get('t',0)<w[1]:
            water[str(w[2])]={}
            water[str(w[2])]['tc']=w[3]
            water[str(w[2])]['t']=w[1]
    return {'supplies' : supplies, 'timerconfigs' : timerconfigs, 'water': water}


@view_config(route_name='harvest', renderer='harvest.mako')
def harvest_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['harvest'] or not request.POST['plant']:
        request.session.flash('Both harvest and plant to be filled out!')
    elif not isinstance(float(request.POST['harvest']),float):
        request.session.flash('Weight must be numerical!')
    elif not isinstance(int(request.POST['plant']),int):
        request.session.flash('This is not a valid plant!')
    else :
        #now check if the plant exists
        plant=int(request.POST['plant'])
        harvest=float(request.POST['harvest'])
        type=str(request.POST.get('type','Fruit'))
        cur=request.db.cursor()
        cur.execute('select count(*) from plants where id = ?', [plant])
        count=cur.fetchone()[0]
        if count !=1 :
            request.session.flash('This plant does not exist!')
        else:
            request.db.execute('insert into harvest (weight, plant, type) values (?, ?, ?)', [harvest, plant, type])
            request.db.commit()
            request.session.flash('Plant harvest was recorded successfully!')
            return HTTPFound(location=request.route_url('home'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    cursor.execute('select * from columns where id !=?', [0])
    columns=cursor.fetchall()
    cursor.execute('select * from slots where id !=?', [0])
    slots=cursor.fetchall()
    cursor.execute('select * from plants where slot!=?',[0])
    plants=cursor.fetchall()
    return {'supplies' : supplies, 'columns' : columns, 'slots' : slots, 'plants' : plants}


@view_config(route_name='log', renderer='log.mako')
def log_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['log'] or not request.POST['plant']:
        request.session.flash('Both log and plant to be filled out!')
    elif not isinstance(int(request.POST['plant']),int):
        request.session.flash('This is not a valid plant!')
    else :
        #now check if the plant exists
        plant=int(request.POST['plant'])
        log=request.POST['log']
        cur=request.db.cursor()
        cur.execute('select count(*) from plants where id = ?', [plant])
        count=cur.fetchone()[0]
        if count !=1 :
            request.session.flash('This plant does not exist!')
        else:
            request.db.execute('insert into logs (log, plant) values (?, ?)', [log, plant])
            request.db.commit()
            request.session.flash('Plant log was recorded successfully!')
            return HTTPFound(location=request.route_url('home'))
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    cursor.execute('select * from columns where id !=?', [0])
    columns=cursor.fetchall()
    cursor.execute('select * from slots where id !=?', [0])
    slots=cursor.fetchall()
    cursor.execute('select * from plants where slot!=?',[0])
    plants=cursor.fetchall()
    return {'supplies' : supplies, 'columns' : columns, 'slots' : slots, 'plants' : plants}


@view_config(route_name='pic', renderer='pic.mako')
def pic_view(request):
    if not request.method == 'POST':
        pass
    elif not request.POST['plant']:
        request.session.flash('Both file and plant to be filled out!')
    elif not isinstance(int(request.POST['plant']),int):
        request.session.flash('This is not a valid plant!')
    else :
        #now check if the plant exists
        plant=int(request.POST['plant'])
        pic=request.POST['pic'].file
        bitstream=pic.read()
        #determine filetype
        type=imghdr.what(request.POST['pic'].filename, bitstream)#when second argument is provided, the first is ignored
        if type=='gif' or type=='bmp' or type=='jpeg' or type=='png':
            #come up with a filename
            file_name=os.urandom(16).encode('hex')+'.'+ type
            path = os.path.join(here,'static/images/')
            web_path = os.path.join( '/static/images/', file_name)
            file_path = os.path.join( path, file_name)
            with open(file_path, 'wb') as output_file:
                shutil.copyfileobj(pic, output_file)
            cur=request.db.cursor()
            cur.execute('select count(*) from plants where id = ?', [plant])
            count=cur.fetchone()[0]
            if count !=1 :
                request.session.flash('This plant does not exist!')
            else:
                request.db.execute('insert into pictures (path, plant) values (?, ?)', [web_path, plant])
                request.db.commit()
                request.session.flash('Plant pic was recorded successfully!')
                return HTTPFound(location=request.route_url('home'))
        else:
            request.session.flash('Not a valid file type, only supported filetypes are jpg, bmp, png and gif!')
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id != ?', [0])
    supplies=cursor.fetchall()
    cursor.execute('select * from columns where id !=?', [0])
    columns=cursor.fetchall()
    cursor.execute('select * from slots where id !=?', [0])
    slots=cursor.fetchall()
    cursor.execute('select * from plants where slot!=?',[0])
    plants=cursor.fetchall()
    return {'supplies' : supplies, 'columns' : columns, 'slots' : slots, 'plants' : plants}


@view_config(route_name='list',renderer='list.mako')
def list_view(request):
    cursor=request.db.cursor()
    cursor.execute('select * from supplies where id!=0')
#    supplies=h.convres(cursor.fetchall())
    supplies=cursor.fetchall()
    cursor.execute('select * from columns where id != 0')
    columns=cursor.fetchall()
    cursor.execute('select * from slots where id!=0')
    slots=cursor.fetchall()
    cursor.execute('select * from plants where slot!=0')
    plants=cursor.fetchall()
#    request.session.flash(str(supplies))
 #   supplies=[]
    return {'supplies': supplies, 'columns': columns, 'slots': slots, 'plants': plants}

@view_config(context='pyramid.exceptions.NotFound', renderer='notfound.mako')
def notfound_view(request):
    request.response.status = '404 Not Found'
    return {}
