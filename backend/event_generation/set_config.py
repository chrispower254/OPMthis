import json

config_file = 'config.json'
#config_file = 'configAdidas.json'

def set_filters(filter_json):
    with open(config_file) as f:
        config = json.load(f)


    config['filters'] = filter_json

    with open(config_file, 'w') as f:
        json.dump(config, f)

    print("Set filters finished")


def set_settings(settings_json):
    with open(config_file) as f:
        config = json.load(f)


    print(settings_json)
    config['baseUrl'] = settings_json['baseUrl']
    config['eventAttributes'] = settings_json['eventAttributes']
    config['kafkaSettings']['topic'] = settings_json['kafkaSettings']['topic']
    config['kafkaSettings']['bootstrapServers'] = settings_json['kafkaSettings']['bootstrapServers']
    config['opmSettings']['eventLogType'] = settings_json['opmSettings']['eventLogType']
    config['opmSettings']['opmAlgo'] = settings_json['opmSettings']['opmAlgo']
    config['opmSettings']['processNetType'] = settings_json['opmSettings']['processNetType']
    config['opmSettings']['heuMinConfig']['dependency'] = settings_json['opmSettings']['heuMinConfig']['dependency']

    with open(config_file, 'w') as f:
        json.dump(config, f)

    print("Set settings finished")

