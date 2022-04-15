import uuid

def gen_id():
    id = str(uuid.uuid4())[:8]
    return id
