# Importing necessary libraries

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import nltk

# Sample data

# So this dataset contains 4 concepts : Music, Technology, Food, Global warming and pollution.
dataset = ["The amount of pollution is increasing day by day",
           "The concert was just great",
           "Gordan Ramsay cooks great",
           "Google is introducing new technology",
           "AI Robots are examples of great technology",
           "All the people were singing in the concert",
           "There is a campaign to stop pollution and global warming"
           ]

dataset = [line.lower() for line in dataset]

vectorizer = TfidfVectorizer()

# This X is now contains the Tfidf Model
X = vectorizer.fit_transform(dataset)

# n_components = no_of_concepts
lsa = TruncatedSVD(n_components = 4, n_iter = 200)

# This fit_transform will return only V(r x n) matrix
# r = number of concepts
# n = probability of the word related to that concept

lsa.fit(X)
terms = vectorizer.get_feature_names()

# lsa.components_ contains all the rows

concept_words = {}
for i, probability in enumerate(lsa.components_):
    component_terms = zip(terms, probability)
    # Sorting by the probability not by the term
    sorted_terms = sorted(component_terms, key = lambda x:x[1], reverse = True)
    sorted_terms = sorted_terms[:10]

    concept_words["Concept "+str(i)] = sorted_terms

for key in concept_words.keys():
    sentence_scores = []

    for sent in dataset:
        words = nltk.word_tokenize(sent)
        score = 0

        for word in words:
            for word_with_score in concept_words[key]:
                if word == word_with_score[0]:
                    score += word_with_score[1]

        sentence_scores.append(score)

    print("\n{}: ".format(key))
    for sentence_score in sentence_scores:
        print(sentence_score)
