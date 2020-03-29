#Temitope Akinwale 16308933
#This file is where I implement my conditional exponential classifier
# I use the conditional exponential classifier within nltk to train my model
#I then evaluate it by seeing how accurate it is 


#importing libraries 
import json
import nltk
import random
import balance_dataset


SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

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
        if i >= SAMPLE_SIZE: 
            break

#print out the number of entries
print(i)


# should be randomised here
random.shuffle(feature_data)
# split the data into training and testing data
training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]
# # train the classifier with the training data
classifier = nltk.ConditionalExponentialClassifier.train(training_data)
# # print out the classifiers accuracy on the test data
print(nltk.classify.accuracy(classifier, test_data))

#save classifier so we don't have to retrain it every time we want to use it
# classifier_file = open(conditional_exponential_classifier.pickle', 'wb')
# pickle.dump(classifier, classifier_file)
# classifier_file.close()


