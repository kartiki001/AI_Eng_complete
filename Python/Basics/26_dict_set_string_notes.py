
# ========================================================================
# Part 1: Python Dictionaries
# ========================================================================

# 1. What is a dictionary?
#
# A dictionary is a collection of key-value pairs.
#
# Properties:
#     Ordered: Maintains insertion order.
#     Mutable: We can add, update and delete elements.
#     No duplicate keys: Each key must be unique.
#     Keys must be immutable (e.g. strings, numbers, tuples).
#     Values can be of any data type.
#
# Syntax:
#     dictionary = {key: value}
#
# Example:

student = {
    "name": "Alice",
    "age": 22,
    "course": "AI Engineering"
}

print(student)

# Creating an empty dictionary
my_dict = {}
my_dict = dict()

# Accessing dictionary values using keys

student = {
    "name": "Alice",
    "age": 22,
    "course": "AI Engineering"
}

print(student["name"])    # Alice
print(student["age"])     # 22
print(student["course"])  # AI Engineering

# IMPORTANT:
# Accessing a key that does not exist using [] raises KeyError.

# print(student["city"])  # KeyError


# ========================================================================
# 2. get() Method
# ========================================================================

# get() returns the value associated with a key.
#
# Syntax:
#     dictionary.get(key)
#     dictionary.get(key, default_value)
#
# Difference:
#     dictionary[key] -> Raises KeyError if key does not exist.
#     dictionary.get(key) -> Returns None if key does not exist.
#     dictionary.get(key, default) -> Returns default if key does not exist.

student = {
    "name": "Alice",
    "age": 22
}

print(student.get("name"))          # Alice
print(student.get("age"))           # 22
print(student.get("city"))          # None
print(student.get("city", "Unknown"))  # Unknown


# ========================================================================
# 3. keys() Method
# ========================================================================

# keys() returns all the keys in a dictionary.
#
# Syntax:
#     dictionary.keys()

student = {
    "name": "Alice",
    "age": 22,
    "course": "AI"
}

print(student.keys())

# Output:
# dict_keys(['name', 'age', 'course'])

# Converting keys into a list

keys_list = list(student.keys())
print(keys_list)

# ['name', 'age', 'course']


# ========================================================================
# 4. values() Method
# ========================================================================

# values() returns all the values in a dictionary.
#
# Syntax:
#     dictionary.values()

student = {
    "name": "Alice",
    "age": 22,
    "course": "AI"
}

print(student.values())

# Output:
# dict_values(['Alice', 22, 'AI'])

# Converting values into a list

values_list = list(student.values())
print(values_list)


# ========================================================================
# 5. items() Method
# ========================================================================

# items() returns all key-value pairs as tuples.
#
# Syntax:
#     dictionary.items()
#
# Each item contains:
#     (key, value)

student = {
    "name": "Alice",
    "age": 22,
    "course": "AI"
}

print(student.items())

# Output:
# dict_items([
#     ('name', 'Alice'),
#     ('age', 22),
#     ('course', 'AI')
# ])

# Looping through items()

for key, value in student.items():
    print(key, value)

# name Alice
# age 22
# course AI


# ========================================================================
# 6. Adding and Updating Dictionary Elements
# ========================================================================

# Adding a new key-value pair:
#     dictionary[new_key] = value
#
# Updating an existing value:
#     dictionary[existing_key] = new_value

student = {
    "name": "Alice",
    "age": 22
}

# Adding
student["city"] = "Pune"
print(student)

# Updating
student["age"] = 23
print(student)


# ========================================================================
# 7. update() Method
# ========================================================================

# update() adds new key-value pairs or updates existing keys.
#
# Syntax:
#     dictionary.update(other_dictionary)
#
# If a key already exists, its value gets updated.
# If a key does not exist, it gets added.

student = {
    "name": "Alice",
    "age": 22
}

student.update({
    "age": 23,
    "city": "Pune",
    "course": "AI Engineering"
})

print(student)

# Output:
# {
#     'name': 'Alice',
#     'age': 23,
#     'city': 'Pune',
#     'course': 'AI Engineering'
# }


# ========================================================================
# 8. Removing Dictionary Elements
# ========================================================================

# pop(key) removes the specified key and returns its value.

student = {
    "name": "Alice",
    "age": 22,
    "city": "Pune"
}

removed_value = student.pop("age")

print(removed_value)  # 22
print(student)

# popitem() removes and returns the last inserted key-value pair.

student = {
    "name": "Alice",
    "age": 22,
    "city": "Pune"
}

removed_item = student.popitem()
print(removed_item)  # ('city', 'Pune')
print(student)

# del removes a specific key.

del student["age"]
print(student)

# clear() removes all elements.

student.clear()
print(student)  # {}


# ========================================================================
# 9. Checking Keys in a Dictionary
# ========================================================================

# in checks whether a KEY exists in a dictionary.
# not in checks whether a KEY does not exist.

student = {
    "name": "Alice",
    "age": 22
}

print("name" in student)       # True
print("city" in student)       # False
print("city" not in student)   # True

# IMPORTANT:
# The in operator checks dictionary KEYS, not values.

print("Alice" in student)      # False


# ========================================================================
# 10. Looping Through Dictionaries
# ========================================================================

student = {
    "name": "Alice",
    "age": 22,
    "course": "AI"
}

# Loop through keys (default behavior)

for key in student:
    print(key)

# Loop through values

for value in student.values():
    print(value)

# Loop through key-value pairs

for key, value in student.items():
    print(key, ":", value)


# ========================================================================
# 11. Nested Dictionaries
# ========================================================================

# A dictionary can contain another dictionary.

students = {
    "student1": {
        "name": "Alice",
        "age": 22
    },
    "student2": {
        "name": "Bob",
        "age": 24
    }
}

print(students["student1"]["name"])  # Alice
print(students["student2"]["age"])   # 24


# ========================================================================
# 12. Dictionary Comprehension
# ========================================================================

# Dictionary comprehension creates dictionaries in one line.
#
# Syntax:
#     {key_expression: value_expression for item in iterable}

numbers = [1, 2, 3, 4, 5]

squares = {num: num ** 2 for num in numbers}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary comprehension with condition

even_squares = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(even_squares)

# {2: 4, 4: 16}


# ========================================================================
# Part 2: Python Sets
# ========================================================================

# 1. What is a set?
#
# A set is an unordered collection of unique elements.
#
# Properties:
#     Unordered: No guaranteed positional order.
#     Mutable: We can add and remove elements.
#     No duplicates: Duplicate values are automatically removed.
#     No indexing or slicing.
#     Elements must be hashable (e.g. numbers, strings, tuples).
#
# Example:

numbers = {10, 20, 30, 40}

print(numbers)

# Duplicate values are automatically removed.

numbers = {10, 20, 10, 30, 20}

print(numbers)

# Output:
# {10, 20, 30}

# Creating an empty set

my_set = set()

# IMPORTANT:
# {} creates an empty dictionary, NOT an empty set.

my_dict = {}
my_set = set()

print(type(my_dict))  # <class 'dict'>
print(type(my_set))   # <class 'set'>


# ========================================================================
# 2. Adding Elements to Sets
# ========================================================================

# add() adds a single element.

numbers = {10, 20, 30}

numbers.add(40)
print(numbers)

# Adding an existing element does nothing.

numbers.add(20)
print(numbers)


# ========================================================================
# 3. update() in Sets
# ========================================================================

# update() adds multiple elements from an iterable.
#
# Syntax:
#     set.update(iterable)

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)

# You can also add elements from another set.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

set1.update(set2)

print(set1)


# ========================================================================
# 4. Removing Elements from Sets
# ========================================================================

numbers = {10, 20, 30, 40}

# remove() removes an element.
# Raises KeyError if the element does not exist.

numbers.remove(20)
print(numbers)

# discard() removes an element.
# Does NOT raise an error if the element does not exist.

numbers.discard(100)
print(numbers)

# pop() removes and returns an arbitrary element.
# Do not assume which element will be removed.

removed = numbers.pop()
print(removed)
print(numbers)

# clear() removes all elements.

numbers.clear()
print(numbers)


# ========================================================================
# 5. Checking Elements in Sets
# ========================================================================

numbers = {10, 20, 30, 40}

print(20 in numbers)       # True
print(100 in numbers)      # False
print(100 not in numbers)  # True

# Looping through sets

for num in numbers:
    print(num)

# Remember:
# Sets do not support indexing or slicing.

# print(numbers[0])  # TypeError


# ========================================================================
# 6. Set Operations
# ========================================================================

# Consider two sets:

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


# ------------------------------------------------------------------------
# UNION
# ------------------------------------------------------------------------

# Union combines all unique elements from both sets.
#
# Syntax:
#     A.union(B)
#     A | B

union_result = A.union(B)

print(union_result)

# {1, 2, 3, 4, 5, 6, 7, 8}

# Using operator

print(A | B)


# ------------------------------------------------------------------------
# INTERSECTION
# ------------------------------------------------------------------------

# Intersection returns only common elements.
#
# Syntax:
#     A.intersection(B)
#     A & B

intersection_result = A.intersection(B)

print(intersection_result)

# {4, 5}

print(A & B)


# ------------------------------------------------------------------------
# DIFFERENCE
# ------------------------------------------------------------------------

# Difference returns elements present in A but NOT in B.
#
# Syntax:
#     A.difference(B)
#     A - B

difference_result = A.difference(B)

print(difference_result)

# {1, 2, 3}

print(A - B)

# B - A gives elements present in B but NOT in A.

print(B - A)

# {6, 7, 8}


# ------------------------------------------------------------------------
# SYMMETRIC DIFFERENCE
# ------------------------------------------------------------------------

# Returns elements present in either set,
# but NOT in both sets.
#
# Syntax:
#     A.symmetric_difference(B)
#     A ^ B

symmetric_result = A.symmetric_difference(B)

print(symmetric_result)

# {1, 2, 3, 6, 7, 8}

print(A ^ B)


# ========================================================================
# 7. Subset, Superset and Disjoint Sets
# ========================================================================

A = {1, 2, 3, 4, 5}
B = {1, 2}
C = {10, 20}

# issubset():
# Checks whether every element of B exists in A.

print(B.issubset(A))  # True

# Operator: <=

print(B <= A)         # True


# issuperset():
# Checks whether A contains every element of B.

print(A.issuperset(B))  # True

# Operator: >=

print(A >= B)           # True


# isdisjoint():
# Returns True if two sets have NO common elements.

print(A.isdisjoint(C))  # True
print(A.isdisjoint(B))  # False


# ========================================================================
# 8. Set Comprehension
# ========================================================================

numbers = [1, 2, 2, 3, 3, 4, 5]

# Creating a set using comprehension

squares = {num ** 2 for num in numbers}

print(squares)

# Duplicate results are automatically removed.


# ========================================================================
# 9. Practical Set Example: Removing Duplicates
# ========================================================================

names = ["Alice", "Bob", "Alice", "John", "Bob"]

unique_names = set(names)

print(unique_names)

# Convert back into a list if required.

unique_names_list = list(unique_names)

print(unique_names_list)

# IMPORTANT:
# Converting a list into a set removes duplicates,
# but the original list order is not guaranteed.


# ========================================================================
# Part 3: Python Strings
# ========================================================================

# 1. What is a string?
#
# A string is a sequence of characters.
#
# Properties:
#     Ordered: Characters have positions.
#     Immutable: Cannot modify individual characters.
#     Allows duplicate characters.
#     Supports indexing and slicing.
#
# Example:

name = "Python"

print(name)
print(name[0])   # P
print(name[-1])  # n

# Strings are immutable.

# name[0] = "J"  # TypeError

# Instead, create a new string.

name = "J" + name[1:]

print(name)  # Jython


# ========================================================================
# 2. split() Method
# ========================================================================

# split() breaks a string into a LIST of smaller strings.
#
# Syntax:
#     string.split(separator)
#
# Default separator is whitespace.

text = "Python is useful for AI"

words = text.split()

print(words)

# ['Python', 'is', 'useful', 'for', 'AI']

# Splitting using a specific separator

text = "apple,banana,orange"

fruits = text.split(",")

print(fruits)

# ['apple', 'banana', 'orange']

# Splitting using spaces

text = "AI ML DL"

result = text.split(" ")

print(result)

# Limiting the number of splits

text = "Python is useful for AI Engineering"

result = text.split(" ", 2)

print(result)

# ['Python', 'is', 'useful for AI Engineering']


# ========================================================================
# 3. join() Method
# ========================================================================

# join() combines elements of an iterable into a STRING.
#
# Syntax:
#     separator.join(iterable)
#
# IMPORTANT:
# join() is called on the separator string.
# All elements must be strings.

words = ["Python", "is", "useful"]

sentence = " ".join(words)

print(sentence)

# Python is useful

# Joining using a comma

fruits = ["apple", "banana", "orange"]

result = ", ".join(fruits)

print(result)

# apple, banana, orange

# Joining without any separator

letters = ["A", "I", "M", "L"]

result = "".join(letters)

print(result)

# AIML

# Joining using a hyphen

words = ["AI", "ML", "DL"]

result = "-".join(words)

print(result)

# AI-ML-DL


# ========================================================================
# 4. strip() Method
# ========================================================================

# strip() removes whitespace from BOTH ends of a string.
#
# Related methods:
#     strip()  -> Removes from both ends.
#     lstrip() -> Removes from the left side.
#     rstrip() -> Removes from the right side.

text = "   Python AI   "

print(text.strip())

# Python AI

print(text.lstrip())

# Python AI with trailing spaces

print(text.rstrip())

# Python AI with leading spaces

# strip() does not remove spaces from the middle.

text = "Python   AI"

print(text.strip())

# Python   AI

# Removing specific characters from both ends

text = "###Python###"

print(text.strip("#"))

# Python


# ========================================================================
# 5. replace() Method
# ========================================================================

# replace() replaces one substring with another.
#
# Syntax:
#     string.replace(old, new)
#     string.replace(old, new, count)
#
# Strings are immutable, so replace() returns a NEW string.

text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)

# I like Python

# Original string remains unchanged.

print(text)

# I like Java

# Replacing multiple occurrences

text = "AI is useful. AI is powerful."

result = text.replace("AI", "Artificial Intelligence")

print(result)

# Limiting replacements using count

text = "apple apple apple"

result = text.replace("apple", "orange", 2)

print(result)

# orange orange apple


# ========================================================================
# 6. find() Method
# ========================================================================

# find() returns the index of the FIRST occurrence of a substring.
#
# Syntax:
#     string.find(substring)
#
# If the substring is not found, it returns -1.
# It does NOT raise an error.

text = "Python is useful for AI"

print(text.find("Python"))  # 0
print(text.find("useful"))  # 10
print(text.find("AI"))      # 21
print(text.find("Java"))    # -1

# Searching from a specific position

text = "AI ML AI DL"

print(text.find("AI", 1))  # 6

# IMPORTANT:
# find() returns an index, NOT True or False.


# ========================================================================
# 7. upper() Method
# ========================================================================

# upper() converts all alphabetic characters to uppercase.

text = "Python for AI"

result = text.upper()

print(result)

# PYTHON FOR AI

# Original string remains unchanged.

print(text)


# ========================================================================
# 8. lower() Method
# ========================================================================

# lower() converts all alphabetic characters to lowercase.

text = "PYTHON FOR AI"

result = text.lower()

print(result)

# python for ai

# Original string remains unchanged.

print(text)


# ========================================================================
# 9. Additional Useful String Methods
# ========================================================================

text = "Python for AI"

# capitalize() -> First character uppercase, remaining lowercase.

print(text.capitalize())

# title() -> First character of each word uppercase.

print(text.title())

# startswith() -> Checks whether string starts with given text.

print(text.startswith("Python"))  # True

# endswith() -> Checks whether string ends with given text.

print(text.endswith("AI"))  # True

# count() -> Counts occurrences of a substring.

text = "AI ML AI DL AI"

print(text.count("AI"))  # 3

# isdigit() -> Checks whether all characters are digits.

print("12345".isdigit())  # True

# isalpha() -> Checks whether all characters are alphabets.

print("Python".isalpha())  # True

# isalnum() -> Checks whether all characters are letters or digits.

print("Python123".isalnum())  # True

# isspace() -> Checks whether all characters are whitespace.

print("   ".isspace())  # True


# ========================================================================
# Part 4: Practical AI Engineering Examples
# ========================================================================


# ------------------------------------------------------------------------
# 1. Dictionary: Model Configuration
# ------------------------------------------------------------------------

# Dictionaries are useful for storing model configurations.

model_config = {
    "model_name": "GPT",
    "temperature": 0.7,
    "max_tokens": 1000,
    "top_p": 0.9
}

print(model_config.get("model_name"))

# Updating model configuration

model_config.update({
    "temperature": 0.5,
    "max_tokens": 2000
})

print(model_config)


# ------------------------------------------------------------------------
# 2. Dictionary: API Response
# ------------------------------------------------------------------------

# API responses are frequently represented as JSON.
# JSON objects are commonly converted into Python dictionaries.

api_response = {
    "status": "success",
    "model": "GPT",
    "response": "Artificial Intelligence is transforming technology.",
    "tokens_used": 150
}

print(api_response["response"])
print(api_response.get("tokens_used"))

# Loop through API response

for key, value in api_response.items():
    print(key, ":", value)


# ------------------------------------------------------------------------
# 3. Set: Removing Duplicate Words
# ------------------------------------------------------------------------

text = "AI ML AI DL ML Python"

words = text.split()

unique_words = set(words)

print(unique_words)

# Useful for finding unique words in text datasets.


# ------------------------------------------------------------------------
# 4. Set: Finding Common Words Between Documents
# ------------------------------------------------------------------------

document1 = "Python is useful for AI and ML"
document2 = "Python is useful for Data Science"

words1 = set(document1.lower().split())
words2 = set(document2.lower().split())

# Common words

common_words = words1.intersection(words2)

print(common_words)

# Words unique to document 1

unique_to_doc1 = words1.difference(words2)

print(unique_to_doc1)


# ------------------------------------------------------------------------
# 5. String: Basic Text Preprocessing
# ------------------------------------------------------------------------

text = "   PYTHON is POWERFUL for AI Engineering!   "

# Step 1: Remove leading and trailing spaces.

text = text.strip()

# Step 2: Convert to lowercase.

text = text.lower()

# Step 3: Replace punctuation.

text = text.replace("!", "")

# Step 4: Split into individual words.

words = text.split()

print(words)

# ['python', 'is', 'powerful', 'for', 'ai', 'engineering']

# This demonstrates basic text preprocessing.
# Real-world NLP preprocessing may require additional steps.


# ------------------------------------------------------------------------
# 6. String: Preparing Text for Processing
# ------------------------------------------------------------------------

sentences = [
    "Python is useful",
    "AI is powerful",
    "Machine Learning is interesting"
]

# Convert all sentences into lowercase words.

all_words = []

for sentence in sentences:
    words = sentence.lower().split()
    all_words.extend(words)

print(all_words)

# Finding unique vocabulary

vocabulary = set(all_words)

print(vocabulary)

# Number of unique words

print(len(vocabulary))


# ========================================================================
# Part 5: Quick Revision
# ========================================================================
# ========================================================================
# DICTIONARIES
# ========================================================================

# get(key, default=None)              -> dicti.get(key, default) | Returns value; default is optional (default: None).
# keys()                              -> dicti.keys() | Returns a view of all keys; takes no arguments.
# values()                            -> dicti.values() | Returns a view of all values; takes no arguments.
# items()                             -> dicti.items() | Returns a view of (key, value) tuples; takes no arguments.
# pop(key, default)                   -> dicti.pop(key, default) | Removes key and returns its value; key mandatory, default optional (without default, missing key raises KeyError).
# update(other)                       -> dicti.update(other) | Adds/updates key-value pairs; other is mandatory (dictionary or iterable of pairs).
# popitem()                           -> dicti.popitem() | Removes and returns the last inserted (key, value) tuple; takes no arguments.
# clear()                             -> dicti.clear() | Removes all elements; takes no arguments.


# ========================================================================
# SETS
# ========================================================================

# add(element)                        -> set.add(element) | Adds one element; element mandatory; returns None.
# update(iterable1, iterable2, ...)   -> set.update(iterable1, ...) | Adds elements from one or more iterables; at least one iterable required; returns None.
# remove(element)                     -> set.remove(element) | Removes element; mandatory; raises KeyError if absent; returns None.
# discard(element)                    -> set.discard(element) | Removes element if present; mandatory; no error if absent; returns None.
# pop()                               -> set.pop() | Removes and returns an arbitrary element; takes no arguments; raises KeyError if empty.
# clear()                             -> set.clear() | Removes all elements; takes no arguments; returns None.
# union(other_set, ...)               -> set.union(other_set, ...) | Returns a NEW set containing all unique elements; at least one iterable required.
# intersection(other_set, ...)        -> set.intersection(other_set, ...) | Returns a NEW set containing common elements; at least one iterable required.
# difference(other_set, ...)          -> set.difference(other_set, ...) | Returns a NEW set containing elements in first set but not others; at least one iterable required.
# symmetric_difference(other_set)    -> set.symmetric_difference(other_set) | Returns a NEW set containing elements in either set but not both; one iterable mandatory.
# issubset(other_set)                 -> set.issubset(other_set) | Returns True if all elements of set exist in other_set; one iterable mandatory.
# issuperset(other_set)               -> set.issuperset(other_set) | Returns True if set contains all elements of other_set; one iterable mandatory.
# isdisjoint(other_set)               -> set.isdisjoint(other_set) | Returns True if sets have no common elements; one iterable mandatory.


# ========================================================================
# STRINGS
# ========================================================================

# split(separator=None, maxsplit=-1)  -> string1.split(separator, maxsplit) | Returns a LIST of substrings; separator optional (default: whitespace), maxsplit optional (default: -1 = all splits).
# join(iterable)                      -> separator.join(iterable) | Returns a STRING by joining iterable elements; iterable mandatory (all elements must be strings).
# strip(chars=None)                   -> string1.strip(chars) | Returns a NEW STRING with leading/trailing whitespace removed; chars optional (specific characters to remove).
# lstrip(chars=None)                  -> string1.lstrip(chars) | Returns a NEW STRING with leading characters/whitespace removed; chars optional.
# rstrip(chars=None)                  -> string1.rstrip(chars) | Returns a NEW STRING with trailing characters/whitespace removed; chars optional.
# replace(old, new, count=-1)         -> string1.replace(old, new, count) | Returns a NEW STRING with replacements; old and new mandatory, count optional (default: all occurrences).
# find(substring, start=0, end=len(string1)) -> string1.find(substring, start, end) | Returns the first matching INDEX or -1; substring mandatory, start/end optional.
# upper()                             -> string1.upper() | Returns a NEW STRING in uppercase; takes no arguments.
# lower()                             -> string1.lower() | Returns a NEW STRING in lowercase; takes no arguments.
# capitalize()                        -> string1.capitalize() | Returns a NEW STRING with first character uppercase and remaining characters lowercase; takes no arguments.
# title()                             -> string1.title() | Returns a NEW STRING with the first character of each word uppercase; takes no arguments.
# count(substring, start=0, end=len(string1)) -> string1.count(substring, start, end) | Returns the number of occurrences (integer); substring mandatory, start/end optional.
# startswith(prefix, start=0, end=len(string1)) -> string1.startswith(prefix, start, end) | Returns True/False; prefix mandatory (string or tuple), start/end optional.
# endswith(suffix, start=0, end=len(string1)) -> string1.endswith(suffix, start, end) | Returns True/False; suffix mandatory (string or tuple), start/end optional.


# ========================================================================
# END OF DICTIONARIES, SETS AND STRINGS NOTES
# ========================================================================
