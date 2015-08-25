from tornado import websocket, web, ioloop, escape
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
        data = escape.json.loads(self.request.body.decode("utf-8"))
        type_1 = ['play', 'pause', 'set_time', 'get_info']
        if data['command'] in type_1:
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
            print(payload['data'])
            payload_send = json.dumps(payload)
            client = get_client(payload['destn_id'], cl)
            if client:
                client.write_message(payload_send)
            else:
                print("send msg error")
        else:
            print("unknown command")
