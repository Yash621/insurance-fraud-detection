from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
import os
from flask_cors import CORS, cross_origin
from prediction_Validation_Insertion import prep_validation
from trainingModel import trainModel
from training_validation_Insertion import train_validation
from flask_monitoringdashboard import dashboard
from predictFromModel import prediction

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
dashboard.bind(app)
CORS(app)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


# @app.route("/predict", methods=["POST"])
# @cross_origin()
# def predictRouteClient():


@app.route("/train", methods=["POST"])
@cross_origin()
def trainRouteClient():

    try:
        if request.json["folderPath"] is not None:
            path = request.json["folderPath"]
            train_valObj = train_validation(path)
            train_valObj.train_validation()
            trainModelObj = trainModel()
            trainModelObj.trainingModel()

    except ValueError:
        return Response("Error ocuured !! %s" % ValueError)

    except KeyError:
