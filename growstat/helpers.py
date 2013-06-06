def convres(query):
    data=[]
    for row in query:
        if type=='supply':
            data.append({'id': row[0], 'name': row[1], 'pos' : row[2] })
    return data
