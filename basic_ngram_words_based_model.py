import random
import nltk

# Sample text
text = "This is random text which can be used for text generation, text prediction and text classification."

n = 3

# Creating ngrams
ngrams = {}
words = nltk.word_tokenize(text)
for i in range(len(words) - n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[i+n])

# Testing the word_n_gram
current_gram = ' '.join(words[0:n])
result = current_gram

for i in range(30):
    if current_gram not in ngrams.keys():
        break
    possibilities = ngrams[current_gram]
    next_item = possibilities[random.randrange(len(possibilities))]
    result += ' '.next_item
    rwords = nltk.word_tokenize(result)
    current_gram = ' '.join(rwords[len(rwords) - n: len(rwords)])

print(result)