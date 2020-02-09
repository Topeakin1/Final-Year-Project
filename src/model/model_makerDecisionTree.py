import json
import nltk
import pickle

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not

# read in the data set JSON file and turn it into the format above
feature_data = []
with open('IMDB_reviews.json') as data_file:
    for line in data_file:
        data_item = json.loads(line)
        feature_data.append(({'text': data_item['review_text'].strip()}, data_item['is_spoiler']))

# split the data into training and testing data
# there are 573913 data points
training_data, test_data = feature_data[:500000], feature_data[500000:]
# train the classifier with the training data
classifier = nltk.classify.DecisionTreeClassifier.train(training_data)
# print out the classifiers accuracy on the test data
print(nltk.classify.accuracy(classifier, test_data))

#save classifier so we don't have to retrain it every time we want to use it
classifier_file = open('decision_tree_classifier.pickle', 'wb')
pickle.dump(classifier, classifier_file)
classifier_file.close()