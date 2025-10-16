import re

pattern = r'ab*'
strings = ["a", "ab", "abb", "ac", "b"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
