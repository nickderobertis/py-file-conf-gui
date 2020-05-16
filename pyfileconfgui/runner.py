from typing import Dict, Any

from pyfileconf import Selector, PipelineManager


class PFCRunner:

    def __init__(self):
        self.s = Selector()

    def run(self, path: str) -> Any:
        path_parts = path.split('/')
        if len(path_parts) < 2:
            raise ValueError(f'got invalid path {path}')
        manager_name = path_parts[0]
        run_path = '.'.join(path_parts[1:])
        manager = self.managers[manager_name]
        return manager.run(run_path)

    @property
    def managers(self) -> Dict[str, PipelineManager]:
        return self.s._managers

