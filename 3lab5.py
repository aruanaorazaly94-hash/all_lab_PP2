import re

text = "hello_world example_test notMatched ABC_def"
matches = re.findall(r'[a-z]+_[a-z]+', text)
print(matches)
