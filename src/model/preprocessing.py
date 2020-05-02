#Temitope Akinwale 16308933
#This is my pre-processing implmentation
#Here I complete stopword removal, tokenization and stemming
#I then save the pre-processing to a file


#important libraries 
import json
import nltk
import pickle
import balance_dataset


SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.75)

# read in the data set JSON file and turn it into the format above
feature_data = []
i = 0
stopwords = nltk.corpus.stopwords.words('english')
with open('balanced_reviews.json') as data_file:
# stopwords = nltk.corpus.stopwords.words('english')
    with open('preprocessed_reviews.json') as data_file:
        for line in data_file:
            # load review text from JSON
            data_item = json.loads(line)
            text = data_item['review_text'].strip().lower()
            # split text up into a list of it's words
            text = nltk.word_tokenize(text)
            # make different versions of the same word equal, e.g. go, goes and going all become go
            stemmer = nltk.PorterStemmer()
            # remove stopwords e.g. the, and, a
            text = [stemmer.stem(word) for word in text if word.isalpha() and word not in stopwords]
            text = " ".join(text)
            text = data_item['text']
            feature_data.append(({'text': text}, data_item['is_spoiler']))
            # # save preprocessed reviews so we only do it once
            # review_map = {'text': text, 'is_spoiler': data_item['is_spoiler']}
            # json.dump(review_map, preprocessed_file)
            # preprocessed_file.write("\n")
            i += 1
            if i >= SAMPLE_SIZE:
                break

# preprocessed_file.close()
print(i)



