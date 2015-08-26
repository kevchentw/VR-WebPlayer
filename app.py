import os
from tornado import web, ioloop
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from Api.handler import ApiHandler
from Socket.handler import SocketHandler
from Player.handler import PlayerHandler
from base_handler import BaseHandler
from Admin.handler import AdminHandler

class IndexHandler(BaseHandler):
    def get(self):
        self.render_html("index.html")


BASE_DIR = os.path.dirname(__file__)
STATIC_PATH = os.path.join(BASE_DIR, 'static')
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
MEDIA_PATH = os.path.join(BASE_DIR, 'media')

settings = {
    'template_path': TEMPLATE_PATH,
    'static_path': STATIC_PATH,
    'static_url_prefix': '/static/',
    'media_url_prefix': '/media/',
    "cookie_secret": "ryrt/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "xsrf_cookies": True,
    "ws_server": "ws://localhost:8888/ws",
}

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/api', ApiHandler),
    (r'/player', PlayerHandler),
    (r'/admin', AdminHandler),
    (r'/media/(.*)', web.StaticFileHandler, {'path': MEDIA_PATH}),
    (r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
    (r'/static', web.StaticFileHandler, {'path': STATIC_PATH}),
], **settings)

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
