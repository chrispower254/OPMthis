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

def app_run():
    app.run()