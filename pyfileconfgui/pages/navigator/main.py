import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyfileconfgui.main import PyFileConfGUI

import dash_core_components as dcc
import dash_html_components as html
from dash_keyed_file_browser import KeyedFileBrowser
from dash import dash


def get_layout(gui: 'PyFileConfGUI') -> html.Div:
    return html.Div([
        html.Label('Pyfileconf Items'),
        html.P(json.dumps(gui.structure)),
        KeyedFileBrowser(gui.file_objs),
    ])
