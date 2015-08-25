from clients import cl as clients


def check_client_exist(conn, cl=clients):
    if cl:
        for i in cl:
            if conn == i['conn']:
                return conn
    return False


def remove_client(conn, cl=clients):
    if cl:
        for i in cl:
            if conn == i['conn']:
                cl.remove(i)
                return


def get_client(client_id, cl=clients):
    if cl:
        for i in cl:
            if client_id == i['id'] and i['role'] == "client":
                return i['conn']


def get_clients_id(cl=clients):
    clients_id = []
    for i in cl:
        if i['role'] == "client":
            clients_id.append(i['id'])
    return clients_id


def get_admins(cl=clients):
    admins = []
    for i in cl:
        if i['role'] == "admin":
            admins.append(i['conn'])
    return admins


def change_role(client_id, role, cl=clients):
    if cl:
        for i in cl:
            if client_id == i['id']:
                i['role'] = role


def set_id(old_client_id, new_client_id, cl=clients):
    if cl:
        for i in cl:
            if old_client_id == i['id']:
                i['id'] = new_client_id
