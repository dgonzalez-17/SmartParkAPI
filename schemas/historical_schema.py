def historicalEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'plate': item['plate'],
        'checkInTime': str(item['checkInTime']),
        **({'checkOutTime': str(item['checkOutTime'])} if item['checkOutTime'] is not None else {}),
        'totalValue': item['totalValue'],
        'itsPaid': item['itsPaid']
    }

def historicalsEntity(entity) -> list:
    return [historicalEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, 
    **{i: a[i] for i in a if i != '_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]