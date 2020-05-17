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
        _get_create_entry_layout(gui),
        _get_run_entry_layout(gui),
        _get_edit_entry_layout(gui),
    ])

    return layout


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


def _get_edit_entry_layout(gui: 'PyFileConfGUI') -> html.Div:
    app = gui.app

    layout = html.Div([
        html.H2('Edit Item'),
        html.P(id='edit-item-name-output'),
        html.Div(id='editor-output'),
    ])

    return layout
