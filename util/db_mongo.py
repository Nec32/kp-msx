from pymongo import MongoClient

import config

client = MongoClient(config.MONGODB_URL)

devices = client[config.MONGODB_COLLECTION]['devices']
domains = client[config.MONGODB_COLLECTION]['domains']


def get_device_by_id(device_id):
    return devices.find_one({'id': device_id})


def create_device(entry):
    return devices.insert_one(entry)


def update_device_code(device_id, code):
    return devices.update_one({'id': device_id}, {'$set': {'code': code}})


def update_device_tokens(device_id, token, refresh):
    return devices.update_one({'id': device_id}, {'$set': {'token': token, 'refresh': refresh}})


def update_tokens(token, param, param1):
    return devices.update_one({'token': token}, {'$set': {'token': param, 'refresh': param1}})


def delete_device(device_id):
    return devices.delete_one({'id': device_id})


def update_device_user_agent(device_id, user_agent):
    return devices.update_one({'id': device_id}, {'$set': {'user_agent': user_agent}})

def update_device_settings(device_id, param):
    return devices.update_one({'id': device_id}, {'$set': {'settings': param}})

def get_domain(domain):
    return domains.find_one({'domain': domain})

def add_domain(domain):
    return domains.insert_one({'domain': domain})
