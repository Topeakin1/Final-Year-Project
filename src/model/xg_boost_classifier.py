#Temitope Akinwale 16308933
#This is my XGBoost implmentation 
#I change around the text representation to see which is most accurate
#The text has to be represented as a binary bag of words here
#XGboost has its own libraries it is a form of boosting
#Developed by Tianqi Chen

#importing libraries
import json
import pickle
import balance_dataset
import numpy as np
import xgboost as xgb
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score , f1_score, precision_score, recall_score


SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
spoilers = []
i = 0

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not
with open('preprocessed_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['text']
        feature_data.append(text)#(({'text': text}, data_item['is_spoiler']))
        spoilers.append(1 if data_item['is_spoiler'] else 0)
        i += 1
        if i >= SAMPLE_SIZE: 
            break
       

# preprocessed_file.close()
print(i)


#vector representation 
count_vec = CountVectorizer()
t = count_vec.fit_transform(feature_data) #transforming feature data to a vector
trans_data = t[:TRAIN_TEST_SPLIT]
test_trans_data = t[TRAIN_TEST_SPLIT:]


spoilers = np.array(spoilers)
train = xgb.DMatrix(trans_data, label=spoilers[:TRAIN_TEST_SPLIT]) #transforming the data to a dmatrix
test = xgb.DMatrix(test_trans_data)
param = {'max_depth':2, 'eta':1, 'objective':'binary:logistic' } #tuning hyperparamters 
classifier = xgb.train(param, train, 2)                          #training the xg boost model

print('The DMatrix contents are : ',train)

#generating the accuracy of our prediction
y_pred = classifier.predict(test)
predictions = [round(value) for value in y_pred]
accuracy = accuracy_score(spoilers[TRAIN_TEST_SPLIT:], predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

precision = precision_score(spoilers[TRAIN_TEST_SPLIT:], predictions)
print(precision)

recall = recall_score(spoilers[TRAIN_TEST_SPLIT:], predictions)
print(recall)

f1= f1_score(spoilers[TRAIN_TEST_SPLIT:], predictions)
print(f1)

#save classifier so we don't have to retrain it every time we want to use it
classifier_file = open('xgboost_classifier.pickle', 'wb')
pickle.dump(classifier, classifier_file)
classifier_file.close()



