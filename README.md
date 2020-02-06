# Final-Year-Project

Install NLTK by running pip install --user -U nltk

Potential plan:
* Split data into half spoilers, half non-spoilers, removing any extra data points to make the set even using balance_dataset.py
* Strip each review of words like 'the', 'a', 'and', etc.
* Create two word2vec models, one for spoilers and one for non-spoilers
* Find a way to use the word2vec models to compare the similarity of the text with spoilers/non-spoilers, maybe using [this JavaScript library](https://www.npmjs.com/package/word2vec)