import requests


def get_size(json_response, address_ll):
    point = address_ll
    delta1 = input()
    delta2 = input()
    map_params = {
        "ll": address_ll,
        "spn": ",".join([delta1, delta2]),
        "l": "map",
        "pt": "{},pm2dgl".format(point)
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response
