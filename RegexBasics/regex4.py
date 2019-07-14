import re

sentence1 = "Welcome to the year 2018"
sentence2 = "Just ~% ++++==----------- arrived at @jack's place #fun"
sentence3 = "I             Love                Python"

# \d means any digit.
print(re.sub(r"\d","",sentence1))

# \. means normal dot, \ is protecting dot
print(re.sub(r"[@+-=#%\.\']", "", sentence2))

# \w means all the characters [a-zA-Z0-9]
# It will just remove [a-zA-Z0-9] from sentence2
print(re.sub(r"\w", "", sentence2))

# \W means all the special characters 
# It will just remove [all special characters from sentence2
print(re.sub(r"\W", "", sentence2))

# \s means single space. \s+ means one or more spaces
# It will just remove one or more spaces with only one space.
print(re.sub(r"\s+"," ", sentence3))

# In sentence2, if single quote is removed from jack's then single s doesn't mean anything so to remove that
print(re.sub(r"\s+[a-zA-Z]\s+", " ", sentence3))
