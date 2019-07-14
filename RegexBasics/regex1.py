import re

sentence = "I was born in 1999"

# . means any character and * means 0 or more characters.
print(re.match(r".*", sentence))

# + means 1 or more character
print(re.match(r".+", sentence))

# i.e all the small and capital letters.
# But it's output will be : "I" because re.match() function finds for first match as after I space comes it stops searching.
print(re.match(r"[a-zA-Z]+", sentence))

# i.e any string which starts with a and which has 0 or 1 b not more than 1.
print(re.match(r"ab?", sentence))
