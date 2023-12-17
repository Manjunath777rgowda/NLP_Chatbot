# Import libraries
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import os
import random
import string


# os.chdir('/home/sunil/Desktop/Great Lakes')
# Load the model
# model = pickle.load(open('finalized_model.sav','rb'))

app = Flask(__name__)
CORS(app, origins='*')


@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    predict_request=[[data['sl'],data['sw'],data['pl'],data['pw']]]
    predict_request=np.array(predict_request)
    print(predict_request)
    prediction = model.predict(predict_request)
    print(prediction)
    # Take the first value of prediction
    output = prediction[0]
    print(output)
    return jsonify(int(output))

@app.route("/dummy", methods=["GET"])
@cross_origin()
def dummy():
    text = ''.join(random.choices(string.ascii_lowercase, k=100))
    print(text)
    return jsonify({"data": text})

@app.route("/health", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Up"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
