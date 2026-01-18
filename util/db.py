import config
import json

if config.IS_SQLITE:
  import util.db_sqlite as db
else:
  import util.db_mongo as db

def get_device_by_id(device_id):
    data = db.get_device_by_id(device_id)
    if data and data.get('code'):
        try:
            data['code'] = json.loads(data.get('code'))
        except:
            data['code'] = None
    return data

def create_device(entry):
    return db.create_device(entry)

def update_device_code(id, codeObject):
    code = json.dumps(codeObject)
    return db.update_device_code(id, code)

def update_device_tokens(id, token, refresh):
    return db.update_device_tokens(id, token, refresh)

def update_device_user_agent(id, user_agent):
    return db.update_device_user_agent(id, user_agent)

def update_device_settings(id, param):
    return db.update_device_settings(id, param)

def get_domain(domain):
    return db.get_domain(domain)

def add_domain(domain):
    return db.add_domain(domain)

def update_tokens(token, newToken, refresh):
    return db.update_tokens(token, newToken, refresh)

def delete_device(id):
    return db.delete_device(id)
