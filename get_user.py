def get_user(data, id):
    return [x for x in data['users'] if x['id'] == id][0]




