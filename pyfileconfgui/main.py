from pyfileconf import Selector

from pyfileconfgui.app import create_app
from pyfileconfgui.index import add_layout
from pyfileconfgui.pfc.extract import full_dict_from_selector


class PyFileConfGUI:

    def __init__(self):
        self.s = Selector()
        self.structure = full_dict_from_selector(self.s)
        self.app = create_app()
        add_layout(self)

    def run_server(self, **kwargs):
        self.app.run_server(**kwargs)

