import json
import nltk
import pickle
import pandas as pd
import matplotlib.pyplot as plt


MAX_NUM_OF_EACH_CATEGORY = 150294


new_dataset_file = open("balanced_reviews.json", 'w')

num_spoilers = 0
num_non_spoilers = 0

with open('IMDB_reviews.json') as data_file:
    for line in data_file:
        is_spoiler = json.loads(line)['is_spoiler']                
        if is_spoiler and num_spoilers < MAX_NUM_OF_EACH_CATEGORY:
            new_dataset_file.write(line)
            num_spoilers += 1
        elif not is_spoiler and num_non_spoilers < MAX_NUM_OF_EACH_CATEGORY:
            new_dataset_file.write(line)
            num_non_spoilers += 1
    data_file.close()
            
print('Number of Non Spoilers:',num_non_spoilers) 
print('Number of spoilers:', num_spoilers)

fig =plt.figure()
ax = fig.add_axes([0,0,1,1])
cases = ['spoiler','Non-spoiler']
values= [num_spoilers, num_non_spoilers]
ax.bar(cases,values)
plt.show()

new_dataset_file.close()


