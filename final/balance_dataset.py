#Temitope Akinwale 16308933
#This file is used to balance my data set. 
#The number of non spoielrs to spoilers was imbalanced
#so i balanced it out.

import json

MAX_NUM_OF_EACH_CATEGORY = 150924 #max number of spoilers and non spoilers


#writing to a 
new_dataset_file = open("balanced_reviews.json", 'w') 

#starting the count at zero
num_spoilers = 0
num_non_spoilers = 0

#open up the json file and load it in
with open('IMDB_reviews.json') as data_file:
    for line in data_file:
        #focusing in on the is_spoiler field
        is_spoiler = json.loads(line)['is_spoiler'] 
        #counting up number of spoilers               
        if is_spoiler and num_spoilers < MAX_NUM_OF_EACH_CATEGORY:
            new_dataset_file.write(line)
            num_spoilers += 1
            
        #counting up number of non spoilers    
        elif not is_spoiler and num_non_spoilers < MAX_NUM_OF_EACH_CATEGORY:
            new_dataset_file.write(line)
            num_non_spoilers += 1
    data_file.close() #closing the json file
            
print('Number of Non Spoilers:',num_non_spoilers) 
print('Number of spoilers:', num_spoilers)

new_dataset_file.close() #closing up the entire file

