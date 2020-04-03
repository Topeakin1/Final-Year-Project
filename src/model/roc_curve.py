#Temitope Akinwale 16308933
#This file is where I implement my roc curve
#This is the main template for generating the curve
#can be used for different classifiers with very little modification
#Here I test it on the naive bayes classifier


#importing the libraries
import json
import pickle
import random
import balance_dataset
from sklearn import metrics
import matplotlib.pyplot as plt

SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
i = 0


with open('preprocessed_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['text']
        feature_data.append(({'text': text}, data_item['is_spoiler']))
        i += 1
        if i< SAMPLE_SIZE:
            break

#opening and loading naive bayes classifier 
classifier_file = open('naive_bayes_classifier.pickle', 'rb')
classifier = pickle.load(classifier_file)


random.shuffle(feature_data) #randomising the data 

training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]

#arrays for roc curve
actual = []
predicted = []
def features(data):
    return data[0]

for data in test_data:
    label = classifier.classify(features(data))
    predicted.append(1 if label else 0) #predicated values
    actual.append(1 if data[1] else 0) #actual values 

#plotting the actaul values with the predicted values 
fpr, tpr, thresholds = metrics.roc_curve(actual, predicted) 

print(fpr)
print(tpr)
print(thresholds)

roc_auc = metrics.auc(fpr, tpr)

#preparing and generating the images
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve for Naive Bayes')
plt.legend(loc="lower right")
plt.show()