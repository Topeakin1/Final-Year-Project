import numpy as np
import nltk
from flask import Flask, request, jsonify, render_template, make_response, json
import pickle
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.text = ""

    def handle_data(self, data):
        self.text += data

app = Flask(__name__, template_folder='.')
model = pickle.load(open('naive_bayes_classifier.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    #prediction = model.classify({'text': request.prediction})
    #prediction = model.classify({'text': request.get_json()['prediction']})
    #print(request.data)

    #prediction = model.classify({ 'text': prediction})
    html_parser = MyHTMLParser()
    html_parser.feed(request.form.get('prediction'))
    print(html_parser.text)
    prediction = model.classify({'text': html_parser.text})
    return f'{prediction}'
    #prediction = model.classify({'text': request.args['prediction']})
    # print('prediction')
    # response = make_response()
    # response.mimetype = 'application/json'
    # response.data = json.dumps({'is_spoiler': prediction})
    # return response
    # return render_template('home.html', prediction_text='The entry submitted is a spoiler : {}'.format(prediction))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True) 

