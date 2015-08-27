from base_handler import BaseHandler


class PhotoHandler(BaseHandler):
    def get(self):
        self.render_html("photo/photo.html")
