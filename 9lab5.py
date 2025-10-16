import re

text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
result = re.sub(r'(?=[A-Z])', ' ', text).strip()
print(result)
