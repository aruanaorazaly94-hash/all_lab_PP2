import re

text = "Hello, world. This is a test"
result = re.sub(r'[ ,.]', ':', text)
print(result)
