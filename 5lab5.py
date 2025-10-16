import re

pattern = r'a.*b$'
strings = ["ab", "a123b", "axyzb", "ac", "b"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
