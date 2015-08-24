from tornado import websocket, web, ioloop
import json
from helper import *
from clients import cl


class ApiHandler(web.RequestHandler):
    @web.asynchronous
    def get(self, *args):
        self.finish()
        client_id = self.get_argument("client_id")
        command = self.get_argument("command")
        video_time = self.get_argument("time", default=None)
        data = {
            "command": command,
            "data": {
                "client_id": client_id,
                'time': video_time,
            }
        }
        data = json.dumps(data)
        client = get_client(client_id, cl)
        print(client_id, data)
        if client:
            client.write_message(data)
        else:
            print("send msg error")

            # for c in cl:
            #     c.write_message(data)

    @web.asynchronous
    def post(self):
        self.finish()
        client_id = self.get_argument("client_id")
        command = self.get_argument("command")
        video_time = self.get_argument("time", default=None)
        data = {
            "command": command,
            "data": {
                "client_id": client_id,
                'time': video_time,
            }
        }
        data = json.dumps(data)
        client = get_client(client_id, cl)
        print(client_id, data)
        if client:
            client.write_message(data)
        else:
            print("send msg error")
