import flask
from model import Model, Rat
import model as ml
from flask_cors import CORS 
from flask import request, jsonify
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib as plt
import seaborn as sns

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

shr = Model('shr.txt', 'Total Domicílios', 'Shr')
rat = Rat()
rch = Model('rch.txt', 'Total Indivíduos', 'Rch')

@app.route('/predict', methods=['POST'])
def predict_all():
    data = request.get_json()
    array = []
    for value in data.values():
        array.append(value)
    rat_pred = rat.get_main_rat(array.copy())
    rat_demographics =  rat.get_demographics(array.copy())
    response = {
        'main_rat': rat_pred['mean'],
        'all_rats': rat_pred['all'],
        'demographic_rats': rat_demographics,
        'shr': shr.evaluate_predictions(array.copy()),
        'rch': rch.evaluate_predictions(array.copy()),
        'time_array': rat.time_array
    }
    return response

app.run()