def earningEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'date': str(item['date']),
        'earnings': item['earnings']
    }

def earningsEntity(entity) -> list:
    return [earningEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, 
    **{i: a[i] for i in a if i != '_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]