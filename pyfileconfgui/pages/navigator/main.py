import json
from typing import TYPE_CHECKING, Dict, List, Union, Sequence

from dash.dependencies import Output, Input
from dash.development.base_component import Component

from pyfileconfgui.component import PFCGuiComponent
from pyfileconfgui.dash_ext.component import DashPythonComponent
from pyfileconfgui.pages.navigator.edit import EditItemComponent

if TYPE_CHECKING:
    from pyfileconfgui.main import PyFileConfGUI

import dash_core_components as dcc
import dash_html_components as html
from dash_keyed_file_browser import KeyedFileBrowser
from dash import dash


def show_running_item(selected_file: Dict[str, str]):
    if not selected_file:
        return dash.no_update
    path = selected_file['key']
    return path


def show_editing_item(selected_file: Dict[str, str]):
    if not selected_file:
        return dash.no_update
    path = selected_file['key']
    return path


class NavigatorComponent(PFCGuiComponent):

    @property
    def layout(self) -> Sequence[Union['DashPythonComponent', Component]]:
        app = self.gui.app

        layout = [
            html.Label('Pyfileconf Items'),
            html.P(json.dumps(self.gui.structure)),
            KeyedFileBrowser(self.gui.file_objs, id='kfb'),
            _get_create_entry_layout(self.gui),
            _get_run_entry_layout(self.gui),
            EditItemComponent('edit-item'),
        ]

        return layout

    def add_callbacks(self, app: dash.Dash) -> None:
        self.add_callback(
            app,
            show_running_item,
            Output('run-input', 'children'),
            [Input('kfb', 'openFile')]
        )
        self.add_callback(
            app,
            self.update_files_after_creating_item,
            Output('kfb', 'files'),
            [Input('create-item-output', 'children')]
        )
        self.add_callback(
            app,
            show_editing_item,
            Output('edit-item-name-output', 'children'),
            [Input('kfb', 'selectedFile')]
        )

    def update_files_after_creating_item(self, updated_message: str):
        self.gui.refresh()
        return self.gui.file_objs


def _get_create_entry_layout(gui: 'PyFileConfGUI') -> html.Div:
    app = gui.app

    layout = html.Div([
        html.H3('Create Item'),
        html.Label('Section Path'),
        dcc.Input(id='section-path-input', placeholder='my.section.path', value=''),
        html.Label('Function/Class Import  (optional)'),
        dcc.Input(id='function-class-import-input', placeholder='from mymod import Stuff', value=''),
        html.Button('Submit', id='create-item-submit-button'),
        html.Div(id='create-item-output')
    ])

    return layout


def _get_run_entry_layout(gui: 'PyFileConfGUI') -> html.Div:
    app = gui.app

    layout = html.Div([
        html.H2('Running Item'),
        html.P(id='run-input'),
        html.Div(id='run-output'),
    ])

    return layout

