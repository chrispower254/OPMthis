from flask import Flask, request
from multiprocessing import Process
from opm_algo.opm_update import opm_update
from event_generation.set_filters import set_filters
import json

app = Flask(__name__)


@app.route('/api/update')
def update():
    global p
    p = Process(target=opm_update,args=('csv', 'heu_min', 'heu_net'))
    p.start()
    return(
        {
            'response': 'Update successful'
        }
    )

@app.route('/api/config/filters/get')
def getConfig():
    f = open('config.json')
    config = json.load(f)
    fields = config['eventAttributes']
    print(fields)
    return(
        {
            'response': fields
        }
    )

@app.route('/api/config/filters/post', methods=['POST'])
def postFilters():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        set_filters(json)
        return "json"
    else:
        return 'Content-Type not supported!'

@app.route('/api/config/filterValues/get',methods=['GET'])
def getFilters():
    f = open('config.json')
    config = json.load(f)
    filter_query = request.args.get('query')
    if filter_query in config['filters']:
        filter_values = config['filters'][filter_query]
    if filter_query not in config['filters']:
        filter_values = ''
    print("test")
    print(filter_query)
    print(filter_values)
    return(
        {
            'response': filter_values
        }
    )


def app_run():
    app.run()