from pyfileconf import Selector

from pyfileconfgui.app import create_app
from pyfileconfgui.index import add_layout


class PyFileConfGUI:

    def __init__(self, s: Selector):
        self.app = create_app()
        add_layout(self.app)

    def run_server(self, **kwargs):
        self.app.run_server(**kwargs)

