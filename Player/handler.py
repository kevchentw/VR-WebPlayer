from base_handler import BaseHandler


class PlayerHandler(BaseHandler):
    def get(self):
        self.render_html("player/player.html")

