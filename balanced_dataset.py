import json

MAX_NUM_OF_EACH_CATEGORY = 150924

if __name__ == "__main__":
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

    new_dataset_file.close()
