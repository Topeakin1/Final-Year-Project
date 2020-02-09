import json
import nltk
import pickle
import random
import balance_dataset

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not

SAMPLE_SIZE = 200#balance_dataset.MAX_NUM_OF_EACH_CATEGORY * 2
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.75)

# read in the data set JSON file and turn it into the format above
feature_data = []
i = 0
stopwords = nltk.corpus.stopwords.words('english')
with open('balanced_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['review_text'].strip().lower()
        # split text up into a list of it's words
        text = nltk.word_tokenize(text)
        # make different versions of the same word equal, e.g. go, goes and going all become go
        stemmer = nltk.PorterStemmer()
        # remove stopwords e.g. the, and, a
        text = [stemmer.stem(word) for word in text if word.isalpha() and word not in stopwords]
        text = " ".join(text)
        feature_data.append(({'text': text}, data_item['is_spoiler']))
        i += 1
        if i >= SAMPLE_SIZE:
            break

# split the data into training and testing data
# should be randomised here
random.shuffle(feature_data)
training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]
# train the classifier with the training data
classifier = nltk.NaiveBayesClassifier.train(training_data)
# print out the classifiers accuracy on the test data
print(nltk.classify.accuracy(classifier, test_data))

#save classifier so we don't have to retrain it every time we want to use it
# classifier_file = open('naive_bayes_classifier.pickle', 'wb')
# pickle.dump(classifier, classifier_file)
# classifier_file.close()
