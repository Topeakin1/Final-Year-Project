import nltk
import pickle

#data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]
training_data =
classifier = nltk.NaiveBayesClassifier.train(training_data)

classifier.classify()

#save classifier so we don't have to retrain it every time we want to use it
classifier_file = open('naive_bayes_classifier.pickle', 'wb')
pickle.dump(classifier, classifier_file)
classifier_file.close()
