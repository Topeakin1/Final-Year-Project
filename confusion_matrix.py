import pandas as pd
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
# stopwords = nltk.corpus.stopwords.words('english')
with open('preprocessed_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['text']
        feature_data.append(({'text': text}, data_item['is_spoiler']))
        