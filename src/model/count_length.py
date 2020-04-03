#Temitope Akinwale 16308933
#This is my word frequency file 
#Here I count the amount of sentences as well as the amount of words per sentence

#import libraries
import json
import balance_dataset
import numpy as np


SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

feature_data = []
wordcounts = []
i = 0
num_sentences = 0
total_sentence_length = 0

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not
with open('balanced_reviews.json') as data_file:
    for line in data_file:
        
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['review_text']
        sentences = text.split('.') #splitting each sentence with a full stop
        num_sentences += len(sentences)
        i += 1
        print(i)
        for sentence in sentences:
            words = sentence.split(' ') #splitting each word with a space
            total_sentence_length += len(words)

#getting average sentence length
average_sentence_length = total_sentence_length / num_sentences

print(f"Average amount of words per sentence length: {average_sentence_length}")

print("Standard deviation", np.std(num_sentences))