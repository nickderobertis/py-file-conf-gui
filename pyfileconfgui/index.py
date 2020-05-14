from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyfileconfgui.main import PyFileConfGUI

import dash_core_components as dcc
import dash_html_components as html
from dash import dash
from dash.dependencies import Input, Output

from pyfileconfgui.pages import navigator


def add_layout(gui: 'PyFileConfGUI'):
    app = gui.app
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname in ('/', '/navigator'):
            return navigator.get_layout(gui)
        else:
            return '404'

