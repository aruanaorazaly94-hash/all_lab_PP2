import re

text = "Hello there, General Kenobi"
matches = re.findall(r'[A-Z][a-z]+', text)
print(matches)

