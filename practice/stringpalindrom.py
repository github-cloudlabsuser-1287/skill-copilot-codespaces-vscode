# write a function to check if a string is a palindrome

def is_palindrome(s):
    if len(s) == 0:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

print(is_palindrome('')) # True
print(is_palindrome('a')) # True
print(is_palindrome('ab')) # False
print(is_palindrome('aba')) # True
print(is_palindrome('abba')) # True
print(is_palindrome('abcba')) # True
print(is_palindrome('abccba')) # True
print(is_palindrome('abccbd')) # False    