import nltk
import json
import pickle
import matplotlib.pyplot as plt 
import numpy as np
from collections import Counter 
  
import string 
  
# Open the file in read mode 
text = open("preprocessed_reviews.json", "r") 


stopwords = []
with open("stopwords.txt", "r") as file: 
    for line in file:
        line = line.strip()
        stopwords.append(line)
    file.close()
    
print(stopwords)
    

# Create an empty dictionary 
d = dict() 
  
# Loop through each line of the file 
stopwords = nltk.corpus.stopwords.words('english')
for line in text: 
    data = json.loads(line)
    line = data['text']
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Convert the characters in line to  
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # Remove the punctuation marks from the line 
    line = line.translate(line.maketrans("", "", string.punctuation)) 
  
    # Split the line into words 
    words = line.split(" ") 
  
    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word not in stopwords:
            if word in d: 
            # Increment count of word by 1 
                d[word] = d[word] + 1
            else: 
            # Add the word to dictionary with count 1 
                d[word] = 1
            

a = sorted(d.items(), key=lambda x: x[1], reverse=True)
top20 = []
count = 0
for word in a:
    if word[0] in stopwords:
        continue
    else:
        count+=1
        top20.append(word)
        
            
#print(top20[:50])


n_groups = len(top20[:20])

vals_films = [x[1] for x in top20[:20]]
legends_films = [x[0] for x in top20[:20]]

fig, ax = plt.subplots(figsize=(10, 8))

index = np.arange(n_groups)
bar_width = 0.75

opacity = 0.6

rects1 = plt.bar(index, vals_films, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Ocurrences')


plt.xlabel('Words')
plt.ylabel('Occurences')
plt.title('Word Frequency')
plt.xticks(index + bar_width, legends_films)
plt.legend()

plt.tight_layout()
plt.show()

            
        
    
    
    


  
# Print the contents of dictionary 
#for key in list(d.keys()): 
#    print(key, ":", d[key]) 
