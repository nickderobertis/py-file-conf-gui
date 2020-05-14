import os
import shutil
from typing import Callable
from copy import deepcopy

from pyfileconf import PipelineManager

from tests.config import BASE_GENERATED_DIR
from tests.input_files.amodule import a_function

PM_FOLDER = os.path.join(BASE_GENERATED_DIR, 'pm')
LOGS_PATH = os.path.join(PM_FOLDER, 'MyLogs')
DEFAULTS_FOLDER_NAME = 'defaults'

PM_DEFAULTS = dict(
    folder=PM_FOLDER,
    name='guipm',
    log_folder=LOGS_PATH,
    default_config_folder_name=DEFAULTS_FOLDER_NAME,
)


def full_pm_setup(**kwargs) -> PipelineManager:
    write_a_function_to_pipeline_dict_file()
    pm = create_pm(**kwargs)
    pm.load()
    return pm


def create_pm(**kwargs) -> PipelineManager:
    all_kwargs = deepcopy(PM_DEFAULTS)
    all_kwargs.update(**kwargs)
    pipeline_manager = PipelineManager(**all_kwargs)
    return pipeline_manager


def delete_pm_project(path: str = PM_FOLDER, logs_path: str = LOGS_PATH):
    all_paths = [
        os.path.join(path, 'defaults'),
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


def pipeline_dict_str_with_obj(func: Callable, func_key: str, func_module: str) -> str:
    return f'from {func_module} import {func.__name__}\n\npipeline_dict = {{\n\t"{func_key}": [{func.__name__}],\n}}\n'


def nested_pipeline_dict_str_with_obj(func: Callable, section_key: str, func_key: str, func_module: str) -> str:
    return f'from {func_module} import {func.__name__}\n\npipeline_dict = {{\n\t"{section_key}": {{\n\t\t"{func_key}": [{func.__name__}],\n\t}},\n}}\n'


def write_a_function_to_pipeline_dict_file(pm_folder: str = PM_FOLDER, nest_section: bool = True):
    file_path = os.path.join(pm_folder, 'pipeline_dict.py')

    if nest_section:
        write_str = nested_pipeline_dict_str_with_obj(
            a_function, 'my_section', 'stuff', 'tests.input_files.amodule'
        )
    else:
        write_str = pipeline_dict_str_with_obj(a_function, 'stuff', 'tests.input_files.amodule')
    with open(file_path, 'w') as f:
        f.write(write_str)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delete', action='store_true')

    args = parser.parse_args()

    if args.delete:
        delete_pm_project()
    else:
        pm = full_pm_setup()
