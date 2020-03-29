#Temitope Akinwale 16308933
#This file is where I generate the word cloud
#This is used for data visualization
#Another way of understanding and analyzing our data set


# importing libraries 
import json
import balance_dataset
from wordcloud import WordCloud
import matplotlib.pyplot as plt


SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY 
TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)

# read in the data set JSON file and turn it into the format above
feature_data = []
all_text = ''
i = 0

#opening the balanced reviews document
with open('balanced_reviews.json') as data_file:
    for line in data_file:
        # load review text from JSON
        data_item = json.loads(line)
        all_text = f"{all_text} {data_item['review_text']}"

#preparing the word cloud
wordcloud = WordCloud().generate(all_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# visualizing the word cloud 
wordcloud = WordCloud(max_font_size=40).generate(all_text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()