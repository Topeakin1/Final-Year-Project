#Temitope Akinwale 16308933
#In this file i implement my API using flask
#I conenct my machine learning model to my API and load in the predictive results 
#I also use a function from my content file which allows the HTML code to be recognised
#This connects my app to my chrome extension.

#importing libraries 
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize
from flask import Flask, request, jsonify, render_template, make_response, json
import pickle
from html.parser import HTMLParser

#html parser to take data in from html pages
class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.text = ""

    def handle_data(self, data):
        self.text += data

#creating flask app and loading in machine learning model
app = Flask(__name__, template_folder='.')
model = pickle.load(open('naive_bayes_classifier.pickle', 'rb'))

#route the app takes to connect to the web
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    #taking in the html code and using the model to predict whether or not it is a spoiler
    html_parser = MyHTMLParser()
    html_parser.feed(request.form.get('prediction'))
    sentence = sent_tokenize(html_parser.text)
    print(html_parser.text)
    prediction = model.classify({'text': sentence}) #classifying the html text
    return f'{prediction}' #return the prediction

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True) #get the results as a json and output whether or not its a spoiler

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)