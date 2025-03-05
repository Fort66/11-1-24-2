import json
from importlib import import_module

from icecream import ic

def load_json_source(
    dir_path=None,
    level=None,
    curent_level=None
):
    if level:
        dir_path = f'{dir_path}/{str(level)}'
    else:
        dir_path = f'{dir_path}'
    with open(f'{dir_path}.json', 'r', encoding='utf-8') as jData:
        jdata = json.load(jData)
        if curent_level:
            return jdata.get(str(curent_level), 'Нет такого значения')
        else:
            return jdata


def load_python_file_source(
    dir_path=None,
    # module_name=None,
    # level=None,
    name_source=None
):
    return import_module(f'{dir_path}').__dict__[name_source]

