from typing import Union, Sequence

import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Output, Input
from dash.development.base_component import Component

from pyfileconfgui.component import PFCGuiComponent
from pyfileconfgui.dash_ext.component import DashPythonComponent
from pyfileconfgui.dash_ext.query import get_triggering_id
from pyfileconfgui.dash_ext.tb import TracebackComponent
from pyfileconfgui.pages.navigator.refresh import is_refresh_trigger, REFRESH_INTERVAL_ID


class ReloadPFCComponent(PFCGuiComponent):
    _should_auto_update: bool = True

    @property
    def layout(self) -> Sequence[Union[DashPythonComponent, Component]]:
        return [
            html.Button('Reload Managers', id='reload-button'),
            html.Div(id='reload-output'),
        ]

    def add_callbacks(self, app: dash.Dash) -> None:
        self.add_callback(
            app,
            self.reload_pfc,
            Output('reload-output', 'children'),
            [Input('reload-button', 'n_clicks'), Input(REFRESH_INTERVAL_ID, 'n_intervals')]
        )
        super().add_callbacks(app)

    def reload_pfc(self, n_clicks: int, n_intervals: int):
        if is_refresh_trigger():
            if self._should_auto_update:
                return ''
            return dash.no_update

        try:
            self.gui.runner.reload()
            self._should_auto_update = True
        except Exception as e:
            self._should_auto_update = False
            return TracebackComponent('reload-pfc-traceback').component
        return 'Reloaded pipeline managers'
