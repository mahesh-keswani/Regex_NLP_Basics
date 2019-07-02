import nltk

paragraph = '''This will be very huge paragrapgh.This will be very huge paragrapgh.
               This is going to be very huge paragrapgh.This is becoming very large paragrapgh.
               This will be very huge paragrapgh.This will be very huge paragrapgh.
               This is going to be very huge paragrapgh.This will be very huge paragrapgh.
               This contains random data feel free to manipulate this paragraph.
               You can add, delete, recreate or modify this paragrapgh.
            '''

words = nltk.word_tokenize(paragraph)

# It will return list of tuples, where each tuple is (word, part_of_speech)
tagged_words = nltk.pos_tag(words)
