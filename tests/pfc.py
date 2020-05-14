import os
import shutil
from copy import deepcopy

from pyfileconf import PipelineManager

from tests.config import BASE_GENERATED_DIR

PM_FOLDER = os.path.join(BASE_GENERATED_DIR, 'pm')
LOGS_PATH = os.path.join(PM_FOLDER, 'MyLogs')
DEFAULTS_FOLDER_NAME = 'custom_defaults'

PM_DEFAULTS = dict(
    folder=PM_FOLDER,
    name='guipm',
    log_folder=LOGS_PATH,
    default_config_folder_name=DEFAULTS_FOLDER_NAME,
)


def create_pm(**kwargs) -> PipelineManager:
    all_kwargs = deepcopy(PM_DEFAULTS)
    all_kwargs.update(**kwargs)
    pipeline_manager = PipelineManager(**all_kwargs)
    return pipeline_manager


def delete_pm_project(path: str = PM_FOLDER, logs_path: str = LOGS_PATH):
    all_paths = [
        os.path.join(path, 'defaults'),
        os.path.join(path, 'custom_defaults'),
        os.path.join(path, 'pipeline_dict.py'),
        logs_path,
    ]
    for path in all_paths:
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
        else:
            # Must not exist, maybe add handling for this later
            pass


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delete', action='store_true')

    args = parser.parse_args()

    if args.delete:
        delete_pm_project()
    else:
        create_pm()