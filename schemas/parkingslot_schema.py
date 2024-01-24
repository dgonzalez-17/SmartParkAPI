def parkingslotEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "number": item["number"],
        "busyStatus": item["busyStatus"]
    }

def parkingslotsEntity(entity) -> list:
    return [parkingslotEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, 
    **{i: a[i] for i in a if i != '_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]