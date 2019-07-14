# Preprocessing list of strings with re.

import re

X = [ "This is a scary #wolf",
      "Welcome to the jungle #missing",
      "112233 the number to know",
      "Remember the name s - john",
      "I             Love      Python"
    ]

for i in range(len(X)):
    X[i] = re.sub(r"\W", " ", X[i])
    X[i] = re.sub(r"\s+[a-z]\s+", " " , X[i], flags = re.I)
    X[i] = re.sub(r"\s+", " " , X[i])
    X[i] = re.sub(r"^\s+", "", X[i])
    X[i] = re.sub(r"\s+$", "", X[i])
    
    print(X[i])
