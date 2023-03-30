import json


def read_data():
    with open('data_file.json', 'r', encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data


def write_data(data):
    with open('data_file.json', 'w', encoding='utf-8') as write_file:
        json.dump(data, write_file)
