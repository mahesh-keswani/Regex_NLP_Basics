import nltk

sentence = "Taj Mahal was built by Emperor Shah Jahan"

words = nltk.word_tokenize(sentence)

tagged_words = nltk.pos_tag(words)

# the function ne_chunks() requires tagged_words for named_entity recognition.
named_entity = nltk.ne_chunks(tagged_words)

# this ne_chunks() return Tree object, inorder to see it
named_entity.draw()

'''
Different entities recognized by ne_chunks() :

1) Organization
2) Person
3) Location
4) Date
5) Time
6) Money
7) Percent
8) Facility
9) GPE (Geographical locations)

'''
