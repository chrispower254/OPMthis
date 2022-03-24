import json

#config_file = 'config.json'
config_file = 'configAdidas.json'

def set_filters(filter_json):
    with open(config_file) as f:
        config = json.load(f)


    config['filters'] = filter_json

    with open(config_file, 'w') as f:
        json.dump(config, f)

    print("Set filters finished")


def set_settings(filter_json):
    with open(config_file) as f:
        config = json.load(f)


    print(filter_json)
    config['baseUrl'] = filter_json['baseUrl']
    config['eventAttributes'] = filter_json['eventAttributes']
    config['kafkaSettings']['topic'] = filter_json['kafkaSettings']['topic']
    config['kafkaSettings']['bootstrapServers'] = filter_json['kafkaSettings']['bootstrapServers']

    with open(config_file, 'w') as f:
        json.dump(config, f)

    print("Set filters finished")

