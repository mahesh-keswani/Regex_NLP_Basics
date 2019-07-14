import re

sentence = "I love Avengers"

# re.sub() is used for substitution
#             kisko_karna_h, kisse_karna_h, sentence

# Suppose if the sentence was "I love Avengers Avengers", this re.sub() will substitute all the occurences of Avengers
print(re.sub(r"Avengers","0", sentence))

# re.I means case insensitive.
# 1 means substitute only 1 matched character.
print(re.sub(r"[a-z]+", "0", sentence, 1, flags = re.I))
