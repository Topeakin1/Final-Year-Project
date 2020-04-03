#Temitope Akinwale 16308933
#This file is where I implement my decision tree classifier
# I use the decision tree within nltk to train my model
#I then evaluate it by seeing how accurate it is 


import json
import nltk
import random
import balance_dataset

SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY #using the blanced data set as my sample size 

#splitting my training and test data
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
i = 0

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not
with open('preprocessed_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['text']
        feature_data.append(({'text': text}, data_item['is_spoiler']))
        i += 1

#printing out number of entries 
print(i)

# randomising the feature data
random.shuffle(feature_data)
# split the data into training and testing data
training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]
# # train the classifier with the training data
classifier = nltk.DecisionTreeClassifier.train(training_data)
# # print out the classifiers accuracy on the test data
print(nltk.classify.accuracy(classifier, test_data))

#save classifier so we don't have to retrain it every time we want to use it
# classifier_file = open('decision_tree_classifier.pickle', 'wb')
# pickle.dump(classifier, classifier_file)
# classifier_file.close()



