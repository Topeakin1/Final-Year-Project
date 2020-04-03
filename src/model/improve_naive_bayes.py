# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:49:33 2020

@author: Top Top
"""

import json
# import nltk
import pickle
import random
import balance_dataset
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB, MultinomialNB,ComplementNB, BernoulliNB

from sklearn.feature_extraction.text import TfidfTransformer




# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not

#SAMPLE_SIZE = 3000000
SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
target = []
i = 0
# stopwords = nltk.corpus.stopwords.words('english')
with open('preprocessed_reviews.json') as data_file:
#with open('preprocessed_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['text']
        feature_data.append(text)
        target.append(data_item['is_spoiler'])
        i += 1
        if i>= SAMPLE_SIZE:
           break
       


# preprocessed_file.close()
print(i)



# split the data into training and testing data
training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]
training_target, test_target = target[:TRAIN_TEST_SPLIT], target[TRAIN_TEST_SPLIT:]

count_vec = CountVectorizer(max_df=0.9, min_df=3, binary = True)
t = count_vec.fit_transform(feature_data)
trans_data = t[:TRAIN_TEST_SPLIT]
test_trans_data = t[TRAIN_TEST_SPLIT:]


tfidf_transformer = TfidfTransformer()
model = tfidf_transformer.fit_transform(trans_data,test_trans_data)


classifier = MultinomialNB()
classifier.fit(model,training_target)
print("The accuracy of the MultinomialNB is:  ",  classifier.score(model,training_target))
#save classifier so we don't have to retrain it every time we want to use it
classifier_file = open('naive_bayes_final.pickle', 'wb')
pickle.dump(classifier, classifier_file)
classifier_file.close()




