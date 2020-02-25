import json
import nltk
import pickle
import random
import balance_dataset

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not

SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
wordcounts = []
i = 0
num_sentences = 0
total_sentence_length = 0
# stopwords = nltk.corpus.stopwords.words('english')
with open('balanced_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        text = data_item['review_text']
        sentences = text.split('.')
        num_sentences += len(sentences)
        i += 1
        print(i)
        for sentence in sentences:
            words = sentence.split(' ')
            # wordcounts.append(len(words))
            total_sentence_length += len(words)
            # average_wordcount = sum(wordcounts)/len(wordcounts)
            #average_sentence_length = (average_wordcount / 150924)
            #print(average_sentence_length)
            # a = sum(wordcounts)/ 150924
            # print(a)

average_sentence_length = total_sentence_length / num_sentences
print(f"Average sentence length: {average_sentence_length}")
            
        


# preprocessed_file.close()

# split the data into training and testing data
# should be randomised here
