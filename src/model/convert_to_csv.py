#Temitope Akinwale 16308933
#This file is where I convert the json file to a csv file
# I believed some algorithms would work better with a csv file
#Didnt find a use for the csv file in the end

#importing libraries
import balance_dataset
import json

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not

SAMPLE_SIZE = balance_dataset.MAX_NUM_OF_EACH_CATEGORY

TRAIN_TEST_SPLIT = int(SAMPLE_SIZE * 0.5)
new_csv_file = open("preprocessed_reviews.json", 'w')

# read in the data set JSON file and turn it into the format above
feature_data = []
i = 0

# data structure for storing training data should be [({'text':'text of paragraph...'}, True/False)]; True/False
# indicates if the text is a spoiler or not
with open('new_csv_file') as data_file:
    for line in data_file:
        # load review text from JSON
        
        data_item = json.loads(line)
        text = data_item['text']
        boolean = data_item['is_spoiler']
        feature_data.append(({'text': text}, data_item['^is_spoiler'])) 
        new_csv_file.write('text + "^" + is_spoiler /n' )
    data_file.close()
    
new_csv_file.close() #closing the csv file
      

