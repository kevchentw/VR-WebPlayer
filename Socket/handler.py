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
                "conn": self
            }
            print(client)
            data = {
                "command": "new_conn",
                "data": {
                    "id": client['id']
                }
            }
            data = json.dumps(data)
            self.write_message(data)
            cl.append(client)

    def on_message(self, data):
        print(data)

    def on_close(self):
        remove_client(self)
