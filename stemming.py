import nltk
from nltk.stem import PorterStemmer

paragraph = '''This will be very huge paragrapgh.This will be very huge paragrapgh.
               This is going to be very huge paragrapgh.This is becoming very large paragrapgh.
               This will be very huge paragrapgh.This will be very huge paragrapgh.
               This is going to be very huge paragrapgh.This will be very huge paragrapgh.
               This contains random data feel free to manipulate this paragraph.
               You can add, delete, recreate or modify this paragrapgh.
            '''
stemmer = PorterStemmer()
sentences = nltk.sent_tokenize(paragraph)

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    new_word = [stemmer.stem(word) for word in words]
    sentences[i] = ' '.join(words) 
