from typing import TYPE_CHECKING, Dict, Sequence, Union

import dash
from dash.development.base_component import Component
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from pyfileconfgui.dash_ext.component import DashPythonComponent


class RouterComponent(DashPythonComponent):

    def __init__(self, id: str, routes: Dict[str, DashPythonComponent]):
        self.routes = routes
        super().__init__(id)

    @property
    def layout(self) -> Sequence[Union['DashPythonComponent', Component]]:
        return [
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content')
        ]

    def add_callbacks(self, app: dash.Dash) -> None:
        self.add_callback(
            app,
            self.display_page,
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )

    def display_page(self, pathname):
        try:
            comp = self.routes[pathname]
            return comp.component
        except KeyError:
            return '404'