from base_handler import BaseHandler
from helper import get_clients_id


class AdminHandler(BaseHandler):

    def get(self):
        data = {"clients": get_clients_id()}
        self.render_html("admin/admin.html", **data)
