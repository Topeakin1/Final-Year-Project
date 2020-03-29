#Temitope Akinwale 16308933
#This is my naive bayes classifier implmentation
#Here I use the naive bayes classifier from nltk
#This is the model that I convert to a pickle file
#- and use for my spoiler detecter 

#important libraries 
import json
import nltk
import pickle
import random
import balance_dataset


SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
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
        if i >= SAMPLE_SIZE: 
            break

print(i) #printing out amount of entries 



# randomising the data to reduce chances of using the same data
random.shuffle(feature_data)
# split the data into training and testing data
training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]
# # train the classifier with the training data
classifier = nltk.NaiveBayesClassifier.train(training_data)
# # print out the classifiers accuracy on the test data
print(nltk.classify.accuracy(classifier, test_data)) 

#save classifier so we don't have to retrain it every time we want to use it
classifier_file = open('naive_bayes_classifier_improved.pickle', 'wb')
pickle.dump(classifier, classifier_file)
classifier_file.close() 






