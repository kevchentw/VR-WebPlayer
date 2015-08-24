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
            if client_id == i['id']:
                return i['conn']


def get_clients_id(cl=clients):
    clients_id = []
    for i in cl:
        clients_id.append(i['id'])
    return clients_id
