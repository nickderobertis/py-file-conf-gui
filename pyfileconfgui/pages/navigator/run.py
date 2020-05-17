from typing import Union, Sequence

import dash
from dash.dependencies import Output, Input
from dash.development.base_component import Component
import dash_html_components as html

from pyfileconfgui.component import PFCGuiComponent
from pyfileconfgui.dash_ext.component import DashPythonComponent


class RunEntryComponent(PFCGuiComponent):

    @property
    def layout(self) -> Sequence[Union['DashPythonComponent', Component]]:
        return [
            html.H2('Running Item'),
            html.P(id='run-input'),
            html.Div(id='run-output'),
        ]

    def add_callbacks(self, app: dash.Dash) -> None:
        self.add_callback(
            app,
            self.run_item,
            Output('run-output', 'children'),
            [Input('run-input', 'children')]
        )
        super().add_callbacks(app)

    def run_item(self, path: str):
        output = self.gui.runner.run(path)
        return str(output)
