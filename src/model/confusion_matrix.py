#Temitope Akinwale 16308933
#This file is where I implement my confusion matrix
#This is the main template for generating the matrix
#can be used for different classifiers with very little modification
#Here I test it on the naive bayes classifier

#import libraries 
import json
import nltk
import pickle
import random
import balance_dataset


SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)


feature_data = []
i = 0

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not
#opening json file and creating data strcture 
with open('preprocessed_reviews.json') as data_file:
    for line in data_file:
        
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['text']
        feature_data.append(({'text': text}, data_item['is_spoiler']))
        i += 1

#opening the naive bayes classifier
classifier_file = open('naive_bayes_classifier.pickle', 'rb')
classifier = pickle.load(classifier_file)

random.shuffle(feature_data) #randomising the data
training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:] #splitting the data

#arrays for confusion matrix
actual = []
predicted = []

def features(data):
    return data[0]

for data in test_data:
    label = classifier.classify(features(data)) #classifying the data
    predicted.append(label) #predictions
    actual.append(data[1]) #actual results

#generating and printing out the confusion matrix 
cm = nltk.ConfusionMatrix(actual, predicted)
print("******CONFUSION MATRIX********")
print(cm)


