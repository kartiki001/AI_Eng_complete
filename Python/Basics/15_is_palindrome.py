def is_palindrome(s1):
    return 'IS PALINDROM' if s1==s1[::-1] else 'NOT A PALINDROME'

s1 = input('Enter a string : ')
print(is_palindrome(s1))
