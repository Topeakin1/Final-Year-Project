#Temitope Akinwale 16308933
#This is my support vector machine implmentation
#Here I use the svm from sklearn 
#The text has to be represented as a vector


#importing libraries 
import json
import balance_dataset
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer


SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
target = []
i = 0

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not
with open('preprocessed_reviews.json') as data_file:
    for line in data_file:
        
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['text']
        feature_data.append(text)
        target.append(data_item['is_spoiler'])
        i += 1
        if i> SAMPLE_SIZE:
            break
       
#print out the amount of entires
print(i)

# split the data into training and testing data
training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]
#splitting the data into test target and training target for the projection
training_target, test_target = target[:TRAIN_TEST_SPLIT], target[TRAIN_TEST_SPLIT:]

#transforming the text representation to a vector
count_vec = CountVectorizer()
vector = count_vec.fit_transform(feature_data) 

#splitting the vector 
trans_data = vector[:TRAIN_TEST_SPLIT]
test_trans_data = vector[TRAIN_TEST_SPLIT:]

#classifying the data with the support vector machine
classifier = svm.SVC()
classifier.fit(trans_data, training_target)
print(classifier.score(test_trans_data, test_target))


#save classifier so we don't have to retrain it every time we want to use it
#classifier_file = open('svm_classifier.pickle', 'wb')
#pickle.dump(classifier, classifier_file)
#classifier_file.close() 




