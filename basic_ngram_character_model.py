import random

# Sample data
text = "This is random text which can be used for text generation, text prediction and text classification."

n = 7

# Creating the ngrams
ngrams = {}
for i in range(len(text) - n):
    gram = text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n])

# Testing ngram model
current_gram = text[0:n]
result = current_gram

for i in range(200):
    if current_gram not in ngrams.keys():
        break
    possibilities = ngrams[current_gram]
    next_item = possibilities[random.randrange(len(possibilities))]

    result += next_item

    current_gram = result[len(result) - n: len(result)]
print(result)
