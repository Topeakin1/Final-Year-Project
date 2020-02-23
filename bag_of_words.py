import nltk
import json
import pickle
import matplotlib.pyplot as plt 
import numpy as np
import balance_dataset
from collections import Counter 
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
  
import string 

SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
i = 0
# stopwords = nltk.corpus.stopwords.words('english')

df = pd.read_json('preprocessed_reviews.json')
print(df)