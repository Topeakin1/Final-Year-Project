#Temitope Akinwale 16308933
#This file is where I attempt to imrpove the performance of my Naive Bayes classifier
#I do this using TF-IDF and CountVectorizer as well as some hyperparamters to increase performance

#importing libraries 
import json
import balance_dataset
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer




# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not

SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
target = []
i = 0
with open('preprocessed_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['text']
        feature_data.append(text)
        target.append(data_item['is_spoiler'])
        i += 1
        if i>= SAMPLE_SIZE:
           break
       
# preprocessed_file.close()
print(i)


# split the data into training and testing data
training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]
training_target, test_target = target[:TRAIN_TEST_SPLIT], target[TRAIN_TEST_SPLIT:]

#vector representation
count_vec = CountVectorizer(max_df=0.9, min_df=3, binary = True)
t = count_vec.fit_transform(feature_data)
trans_data = t[:TRAIN_TEST_SPLIT]
test_trans_data = t[TRAIN_TEST_SPLIT:]

#TF-IDF representation
tfidf_transformer = TfidfTransformer()
model = tfidf_transformer.fit_transform(trans_data,test_trans_data)

#Building a model
classifier = MultinomialNB()
classifier.fit(model,training_target)
print("The accuracy of the MultinomialNB is:  ",  classifier.score(model,training_target)) 


#save classifier so we don't have to retrain it every time we want to use it
#classifier_file = open('naive_bayes_final.pickle', 'wb')
#pickle.dump(classifier, classifier_file)
#classifier_file.close()






