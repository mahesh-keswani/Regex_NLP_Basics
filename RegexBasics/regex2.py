import re

sentence = "I was born in 1999"

print(re.match(r"[a-zA-Z]+", sentence)) # It's output will be only I then it stop seraching.

# It will search in complete string 
print(re.search(r"[a-zA-Z]+", sentence))

# How to find start's with question ?
# -> '^' is used for start's with
if re.match(r"^I",sentence):
    print("Match")
else:
    print("No match")

# How to find end's with question ?
# -> '$' is used for that
if re.search(r"1999$", sentence):
    print("Match")
else:
    print("No match")
