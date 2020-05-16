from copy import deepcopy
from typing import Union, List

from pyfileconf import Selector
from pyfileconf.pipelines.models.collection import PipelineCollection
from pyfileconf.views.object import ObjectView


def full_dict_from_selector(s: Selector) -> dict:
    pc_dict = s._structure.copy()
    out_dict = {}
    pc: PipelineCollection
    # TODO: special handling for _general
    for manager_key, manager_dict in pc_dict.items():
        out_dict[manager_key] = {}
        for key, pc in manager_dict.items():
            if key == '_general':
                # Skip level of _general dict
                out_dict[manager_key].update(_pc_to_dict(manager_dict['_general']))
            else:
                # Specific class dict, keep level
                out_dict[manager_key][key] = _pc_to_dict(pc)
    return out_dict


def _pc_to_dict(pc: PipelineCollection) -> Union[dict, str]:
    out_dict = pc.name_dict.copy()
    value: Union[PipelineCollection, ObjectView, List[ObjectView]]
    if len(out_dict) == 1 and all(isinstance(val, ObjectView) for val in out_dict.values()):
        # TODO: check to make sure this works in all cases
        return list(out_dict.values())[0].name
    for key, value in out_dict.items():
        if isinstance(value, ObjectView):
            # replace with str of name
            out_dict[key] = value.name
        elif isinstance(value, list):
            out_dict[key] = [val.name for val in value]
        elif isinstance(value, PipelineCollection):
            # recursively convert PipelineCollection to dict
            out_dict[key] = _pc_to_dict(value)
        else:
            raise ValueError(f'expected one of PipelineCollection, ObjectView, List[ObjectView], '
                             f'got {value} of type {type(value)}')
    return out_dict