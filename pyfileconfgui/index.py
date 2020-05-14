import dash_core_components as dcc
import dash_html_components as html
from dash import dash
from dash.dependencies import Input, Output

from pyfileconfgui.pages import navigator


def add_layout(app: dash.Dash):
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname in ('/', '/navigator'):
            return navigator.get_layout(app)
        else:
            return '404'

