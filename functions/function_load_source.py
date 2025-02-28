import json


def load_source(
    dir_path=None,
    level=None,
    curent_level=None
):
    with open(f'{dir_path}/{str(level)}.json', 'r', encoding='utf-8') as jData:
        jdata = json.load(jData)
        if curent_level:
            for key in jdata.keys():
                if key == str(curent_level):
                    return jdata[key]
        else:
            return jdata
