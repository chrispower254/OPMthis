from flask import Flask
from multiprocessing import Process
from backend.opm_algo.opm_update import opm_update

app = Flask(__name__)


@app.route('/api/update')
def start():
    global p
    p = Process(target=opm_update,args=('csv', 'heu_min', 'heu_net'))
    p.start()
    return(
        {
            'response': 'Update successful'
        }
    )

def app_run():
    app.run()