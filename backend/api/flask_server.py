from flask import Flask, request
from numpy import source
import multiprocessing
from multiprocessing import Process, Queue
from opm_algo.opm_update import opm_update
from event_generation.set_config import set_settings, set_filters
import os
import sys
import json


app = Flask(__name__)


@app.route('/api/restart')
# API to restart python app
def restart():
    os.execl(sys.executable, 'python', '/Users/christophschroeder/PycharmProjects/OPMthis/backend/main.py', *sys.argv[1:])
    return(
        {
            'response': 'restart triggered'
        }
    )


@app.route('/api/update', methods=['GET'])
# API to load new process net
def update():
    if source == 'kafka':
        config_file = 'config.json'
    elif source == 'adidas':
        config_file = 'configAdidas.json'
    f = open(config_file)
    config = json.load(f)

    global p
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    p = Process(target=opm_update,args=(config,return_dict))
    p.start()
    p.join()
    print(return_dict.values())
    return(
        {
            'response': return_dict.values()
        }
    )

@app.route('/api/config/filters/eventAttribute/get', methods=['GET'])
# API to load column names from config json
def getConfigFiltersEventAttribute():
    if source == 'kafka':
        config_file = 'config.json'
    elif source == 'adidas':
        config_file = 'configAdidas.json'
    f = open(config_file)
    config = json.load(f)

    fields = config['eventAttributes']
    print(fields)
    return(
        {
            'response': fields
        }
    )

@app.route('/api/config/filters/get', methods=['GET'])
# API to load column names from config json
def getConfigFilters():
    if source == 'kafka':
        config_file = 'config.json'
    elif source == 'adidas':
        config_file = 'configAdidas.json'
    f = open(config_file)
    config = json.load(f)

    fields = config['filters']
    print("fields: ")
    print(fields)
    return(
        {
            'response': fields
        }
    )

@app.route('/api/config/filters/post', methods=['POST'])
# API to set filters and store them in config json
def postConfigFilters():
    if source == 'kafka':
        config_file = 'config.json'
    elif source == 'adidas':
        config_file = 'configAdidas.json'
    f = open(config_file)
    config = json.load(f)

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        request_json = request.json
        set_filters(request_json,config,source)
        return "json"
    else:
        return 'Content-Type not supported!'
        

@app.route('/api/config/get', methods=['GET'])
# API to load config json
def getSettings():
    if source == 'kafka':
        config_file = 'config.json'
    elif source == 'adidas':
        config_file = 'configAdidas.json'
    f = open(config_file)
    config = json.load(f)

    fields = config
    return(
        {
            'response': fields
        }
    )

@app.route('/api/config/post', methods=['POST'])
# API to set config json
def postSettings():
    if source == 'kafka':
        config_file = 'config.json'
    elif source == 'adidas':
        config_file = 'configAdidas.json'
    f = open(config_file)
    config = json.load(f)

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        request_json = request.json
        set_settings(request_json,config,source)
        return "json"
    else:
        return 'Content-Type not supported!'


def app_run(source_param):
    global source
    source = source_param
    app.run()
