import importlib
from typing import TYPE_CHECKING, Dict, Optional

from pyfileconf.imports.models.statements.obj import ObjectImportStatement

if TYPE_CHECKING:
    from pyfileconfgui.main import PyFileConfGUI

import dash
from dash.dependencies import Output, Input, State


def add_callbacks(gui: 'PyFileConfGUI'):
    app = gui.app

    @app.callback(Output('run-input', 'children'),
                  [Input('kfb', 'openFile')])
    def show_running_item(selected_file: Dict[str, str]):
        if not selected_file:
            return dash.no_update
        path = selected_file['key']
        return path

    @app.callback(Output('run-output', 'children'),
                  [Input('run-input', 'children')])
    def run_item(path: str):
        output = gui.runner.run(path)
        return str(output)

    @app.callback(Output('create-item-output', 'children'),
                  [Input('create-item-submit-button', 'n_clicks')],
                  (State('section-path-input', 'value'), State('function-class-import-input', 'value')))
    def create_item(n_clicks: int, section_path: str, function_class_import: Optional[str]):
        if not section_path:
            return dash.no_update
        if function_class_import is not None:
            imp = ObjectImportStatement.from_str(function_class_import)
            if len(imp.objs) != 1:
                raise ValueError(f'must have exactly one object import, got {imp.objs}')
            mod = importlib.import_module(imp.module)
            func_or_class = getattr(mod, imp.objs[0])
        else:
            func_or_class = None
        output = gui.runner.create(section_path, func_or_class)
        return f'Created {section_path}'

    @app.callback(Output('kfb', 'files'),
                  [Input('create-item-output', 'children')])
    def update_files_after_creating_item(updated_message: str):
        gui.refresh()
        return gui.file_objs

    @app.callback(Output('edit-item-name-output', 'children'),
                  [Input('kfb', 'selectedFile')])
    def show_editing_item(selected_file: Dict[str, str]):
        if not selected_file:
            return dash.no_update
        path = selected_file['key']
        return path
