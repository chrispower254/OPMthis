import json

config_file = 'config.json'
#config_file = 'configAdidas.json'
def set_filters(filter_json):
    with open(config_file) as f:
        config = json.load(f)

    #for filter in config['filters']:
    #    config['filters'][filter].pop

    config['filters'] = filter_json

    with open(config_file, 'w') as f:
        config = json.dump(config, f)

    print("Set filters finished")

