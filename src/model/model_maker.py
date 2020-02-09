import json
import nltk
import pickle

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not

# read in the data set JSON file and turn it into the format above
feature_data = []

with open('balanced_reviews.json') as data_file:
    for line in data_file:
        data_item = json.loads(line)
        text = data_item['review_text'].strip().lower()
        text = nltk.word_tokenize(text)
        stemmer = nltk.PorterStemmer()
        text = [stemmer.stem(word) for word in text if word.isalpha()]
        feature_data.append(({'text': text}, data_item['is_spoiler']))

# split the data into training and testing data
# should be randomised here
training_data, test_data = feature_data[:200000], feature_data[200000:]
# train the classifier with the training data
classifier = nltk.NaiveBayesClassifier.train(training_data)
# print out the classifiers accuracy on the test data
print(nltk.classify.accuracy(classifier, test_data))

#save classifier so we don't have to retrain it every time we want to use it
# classifier_file = open('naive_bayes_classifier.pickle', 'wb')
# pickle.dump(classifier, classifier_file)
# classifier_file.close()
