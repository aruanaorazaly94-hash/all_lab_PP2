def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example
print(is_palindrome("Madam"))
print(is_palindrome("Hello"))
