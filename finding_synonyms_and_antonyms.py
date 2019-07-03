# Finding synonyms and antonyms of words

from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        synonymns.append(s.name())

        for a in s.antonyms():
            antonyms.append(a.name())

print(synonyms)
print(antonyms)
