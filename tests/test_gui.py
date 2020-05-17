

# TODO [$5ec1b24c55d79800078281a1]: real tests
from pyfileconfgui import PyFileConfGUI
from tests.pfc import full_pm_setup


def test_create_gui():
    pm = full_pm_setup()
    gui = PyFileConfGUI()
