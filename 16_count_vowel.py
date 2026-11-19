def count_vowel(str1):
    count = 0
    for i in str1:
        if i in 'AEIOUaeiou':
            count+=1
    return count

s1 =  input("Enter a string : ")
print(count_vowel(s1))