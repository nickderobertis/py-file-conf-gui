from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from pyfileconfgui.main import PyFileConfGUI

import dash
from dash.dependencies import Output, Input


def add_callbacks(gui: 'PyFileConfGUI'):
    app = gui.app

    @app.callback(Output('run-input', 'children'),
                  [Input('kfb', 'selectedFile')])
    def show_running_item(selected_file: Dict[str, str]):
        if not selected_file:
            return dash.no_update
        print(f'got selected file {selected_file}')
        path = selected_file['key']
        return path

    @app.callback(Output('run-output', 'children'),
                  [Input('run-input', 'children')])
    def run_item(path: str):
        output = gui.runner.run(path)
        return str(output)
