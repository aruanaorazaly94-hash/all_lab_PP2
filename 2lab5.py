import re

pattern = r'ab{2,3}'
strings = ["abb", "abbb", "ab", "a", "abbbb"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
