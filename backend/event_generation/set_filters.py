import json


def set_filters(filter_json):
    with open('config.json') as f:
        config = json.load(f)

    #for filter in config['filters']:
    #    config['filters'][filter].pop

    config['filters'] = filter_json

    with open('config.json', 'w') as f:
        config = json.dump(config, f)

    print("Set filters finished")

