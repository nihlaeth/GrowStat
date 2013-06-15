from pyramid.view import view_config
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.httpexceptions import HTTPFound
#import helpers as h

@view_config(route_name='home', renderer='home.mako')
def home_view(request):
    return {'totalharvest': 0, 'totalgrowth': 0, 'totalliveplants': 0, 'averageph': 7, 'averageec': 3, 'averagetemp': 23, 'averagehum': 50}

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
