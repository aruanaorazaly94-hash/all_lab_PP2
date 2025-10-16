import re

text = "SplitAtUpperCaseLetters"
parts = re.findall(r'[A-Z][^A-Z]*', text)
print(parts)
