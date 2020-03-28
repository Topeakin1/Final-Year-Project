# import pandas as pd
import json
import nltk
import pickle
import random
import balance_dataset
from wordcloud import WordCloud
import matplotlib.pyplot as plt


SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
all_text = ''
i = 0
# stopwords = nltk.corpus.stopwords.words('english')
with open('balanced_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        all_text = f"{all_text} {data_item['review_text']}"

# classifier_file = open('naive_bayes_classifier.pickle', 'rb')
# classifier = pickle.load(classifier_file)

# random.shuffle(feature_data)
# training_data, test_data = feature_data[:TRAIN_TEST_SPLIT], feature_data[TRAIN_TEST_SPLIT:]

wordcloud = WordCloud().generate(all_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
        