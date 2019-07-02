import numpy as np
import nltk
import re
import heapq

paragraph = '''This will be very huge paragrapgh.This will be very huge paragrapgh.
               This is going to be very huge paragrapgh.This is becoming very large paragrapgh.
               This will be very huge paragrapgh.This will be very huge paragrapgh.
               This is going to be very huge paragrapgh.This will be very huge paragrapgh.
               This contains random data feel free to manipulate this paragraph.
               You can add, delete, recreate or modify this paragrapgh.
            '''

sentences = nltk.sent_tokenize(paragraph)

# Preprocessing the data
for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub(r"\s+", " ", sentences[i])
    sentences[i] = re.sub(r"\W", " ", sentences[i])

# Creating the histogram
word_count = {}
for sent in sentences:
    words = nltk.word_tokenize(sent)

    for word in words:
        if word not in word_count.keys():
            word_count[word] = 1
        else:
            word_count[word] += 1

freq_words = heapq.nlargest(100, word_count, key = word_count.get)

# Creating the idf for words
word_idfs = {}

for word in freq_words:
    doc_count = 0

    for sent in sentences:
        if word in nltk.word_tokenize(sent):
            doc_count += 1

    word_idfs[word] = np.log( (len(sentences) / doc_count) + 1)

# TF matrix

tf_matrix = {}
for word in freq_words:
    doc_tf = []

    for sent in sentences:
        frequency = 0

        for w in nltk.word_tokenize(word):
            if word == w:
                frequency += 1

        tf_word = frequency / len(nltk.word_tokenize(sent))
        doc_tf.append(tf_word)

    tf_matrix[word] = doc_tf

# TF-IDF calculation

tfidf_matrix = []
for word in tf_matrix.keys():
    tfidf = []

    for value in tf_matrix[word]:
        score = value * word_idfs[word]
        tfidf.append(score)

    tfidf_matrix.append(tfidf)

X = np.asarray(tfidf_matrix)
X = np.transpose(X)
    for 
