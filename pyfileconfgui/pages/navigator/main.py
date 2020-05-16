import json
from typing import TYPE_CHECKING, Dict, List

from dash.dependencies import Output, Input

if TYPE_CHECKING:
    from pyfileconfgui.main import PyFileConfGUI

import dash_core_components as dcc
import dash_html_components as html
from dash_keyed_file_browser import KeyedFileBrowser
from dash import dash


def get_layout(gui: 'PyFileConfGUI') -> html.Div:
    app = gui.app

    layout = html.Div([
        html.Label('Pyfileconf Items'),
        html.P(json.dumps(gui.structure)),
        KeyedFileBrowser(gui.file_objs, id='kfb'),
        html.H2('Running Item'),
        html.P(id='run-input'),
        html.Div(id='run-output'),
    ])

    return layout
