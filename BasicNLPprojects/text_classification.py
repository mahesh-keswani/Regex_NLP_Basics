# Text classification using cornell sentiment analysis dataset

# Importing libraries
import numpy as np 
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files # For loading the files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
# getting data
#load_files will load the files from text_sentoken and create the classes for them.
reviews = load_files('txt_sentoken/') 
X, y = reviews.data, reviews.target

# processing the data
corpus = []
for i in range(len(X)):
    review = re.sub(r'/W',' ',str(X[i]))
    review = review.lower()
    review = re.sub(r'\s+[a-z]\s+',' ', review, flags = re.I)
    review = re.sub(r'\s+', ' ',review)
    review = re.sub(r'[a-z]\s+',' ',review)
    corpus.append(review)

vectorizer = TfidfVectorizer(max_features = 2000, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size = 0.25)

classifier = LogisticRegression()
classifier.fit(train_x, train_y)

prediction = classifier.predict(test_x)

print(confusion_matrix(test_y, prediction))

# Storing as pickle files
with open('train_x.pickle','wb') as f:
    pickle.dump(X, f)

with open('train_y.pickle','wb') as f:
    pickle.dump(y, f)

with open('classifier.pickle','wb') as f:
    pickle.dump(classifier, f)

with open('vectorizer.pickle','wb') as f:
    pickle.dump(vectorizer, f)