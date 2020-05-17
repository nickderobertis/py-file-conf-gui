import importlib
from typing import TYPE_CHECKING, Dict, Optional

from pyfileconf.imports.models.statements.obj import ObjectImportStatement

if TYPE_CHECKING:
    from pyfileconfgui.main import PyFileConfGUI

import dash
from dash.dependencies import Output, Input, State


def add_callbacks(gui: 'PyFileConfGUI'):
    app = gui.app

    @app.callback(Output('run-output', 'children'),
                  [Input('run-input', 'children')])
    def run_item(path: str):
        output = gui.runner.run(path)
        return str(output)
