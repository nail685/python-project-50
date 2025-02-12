import json


def json_formatter(data_dict):
    return json.dumps(data_dict, indent=4)
