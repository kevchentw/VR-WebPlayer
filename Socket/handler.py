from tornado import websocket, web, ioloop
import json
from .helper import *
from helper import *
from clients import cl
import time


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if not check_client_exist(self):
            client = {
                "id": id_generator(),
                "conn": self,
                "role": "client"
            }
            print(client)
            data = {
                "command": "new_conn",
                "destn_role": "client",
                "destn_id": client['id'],
                "data": {
                    "id": client['id']
                }
            }
            data = json.dumps(data)
            self.write_message(data)
            cl.append(client)
            self.send_device_list()

    def on_message(self, data):
        send_to_client = ['play', 'pause', 'set_time', 'set_volume', 'get_info']
        send_to_admin = ['send_info']
        data = json.loads(data)
        comm = data['command']
        if comm in send_to_admin:
            payload = {
                "command": data['command'],
                "destn_role": "admin",
                "destn_id": "0000",
                "send_to": "admin",
                "data": {
                }
            }
            if data['data']:
                payload['data'] = data['data']
            payload_send = json.dumps(payload)
            admins = get_admins(cl)
            if admins:
                for i in admins:
                    i.write_message(payload_send)
        if comm == "change_role":
            change_role(data['data']['client_id'], data['data']['new_role'])
            self.send_device_list()
        if comm == "set_id":
            set_id(data['data']['client_id'], data['data']['new_client_id'])
            self.send_device_list()
        if data['command'] in send_to_client:
            payload = {
                "command": data['command'],
                "destn_role": "client",
                "destn_id": data['destn_id'],
                "send_to": "client",
                "data": {
                }
            }
            if data['data']:
                payload['data'] = data['data']
            payload_send = json.dumps(payload)
            client = get_client(payload['destn_id'], cl)
            if client:
                client.write_message(payload_send)
            else:
                print("send msg error")
        print(data)

    def on_close(self):
        remove_client(self)
        self.send_device_list()

    def send_device_list(self):
        data = {
            "command": "device_list",
            "destn_role": "admin",
            "destn_id": "0000",
            "data": {
                "devices": get_clients_id()
            }
        }
        admins = get_admins(cl)
        if admins:
            for i in admins:
                i.write_message(data)
