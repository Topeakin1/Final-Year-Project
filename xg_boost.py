import json
import nltk
import pickle
import random
import balance_dataset
import numpy as np
import xgboost as xgb
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score


# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not

SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
spoilers = []
i = 0
# stopwords = nltk.corpus.stopwords.words('english')
with open('preprocessed_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['text']
        # # split text up into a list of it's words
        # text = nltk.word_tokenize(text)
        # # make different versions of the same word equal, e.g. go, goes and going all become go
        # stemmer = nltk.PorterStemmer()
        # # remove stopwords e.g. the, and, a
        # text = [stemmer.stem(word) for word in text if word.isalpha() and word not in stopwords]
        # text = " ".join(text)
        feature_data.append(text)#(({'text': text}, data_item['is_spoiler']))
        spoilers.append(1 if data_item['is_spoiler'] else 0)
        # # save preprocessed reviews so we only do it once
        # review_map = {'text': text, 'is_spoiler': data_item['is_spoiler']}
        # json.dump(review_map, preprocessed_file)
        # preprocessed_file.write("\n")
        i += 1
        if i >= SAMPLE_SIZE:
            break

# preprocessed_file.close()
print(i)

# split the data into training and testing data
# should be randomised here
# random.shuffle(feature_data)
# training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]
# # train the classifier with the training data
# classifier = nltk.NaiveBayesClassifier.train(training_data)
# # print out the classifiers accuracy on the test data
# print(nltk.classify.accuracy(classifier, test_data))

count_vec = CountVectorizer()
t = count_vec.fit_transform(feature_data)
trans_data = t[:TRAIN_TEST_SPLIT]#count_vec.fit_transform(training_data)
test_trans_data = t[TRAIN_TEST_SPLIT:]#count_vec.fit_transform(test_data)

# feature_data = np.array(trans_data.toarray())
spoilers = np.array(spoilers)
train = xgb.DMatrix(trans_data, label=spoilers[:TRAIN_TEST_SPLIT])
test = xgb.DMatrix(test_trans_data)
param = {'max_depth':2, 'eta':1, 'objective':'binary:logistic' }
classifier = xgb.train(param, train, 2)

y_pred = classifier.predict(test)
predictions = [round(value) for value in y_pred]
accuracy = accuracy_score(spoilers[TRAIN_TEST_SPLIT:], predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

#save classifier so we don't have to retrain it every time we want to use it
classifier_file = open('xgboost_classifier.pickle', 'wb')
pickle.dump(classifier, classifier_file)
classifier_file.close()


