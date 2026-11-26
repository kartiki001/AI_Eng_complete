
# ========================================================================
# Part 1: List Comprehension
# ========================================================================

# 1. What is List Comprehension?
#
# List comprehension provides a shorter way to create a new list.
#
# Instead of writing a for loop and appending elements,
# we can create the list in a single line.
#
# Syntax:
#     [expression for item in iterable]
#
# expression -> What we want to store.
# item       -> Each element from the iterable.
# iterable   -> List, tuple, range, etc.

numbers = [1, 2, 3, 4, 5]

# Using a normal for loop

squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)

# [1, 4, 9, 16, 25]

# Using list comprehension

squares = [num ** 2 for num in numbers]

print(squares)

# [1, 4, 9, 16, 25]


# ========================================================================
# 2. List Comprehension with Conditions
# ========================================================================

# Syntax:
#     [expression for item in iterable if condition]
#
# The element is included only if the condition is True.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)

# [2, 4, 6, 8]

# Finding odd numbers

odd_numbers = [num for num in numbers if num % 2 != 0]

print(odd_numbers)

# [1, 3, 5, 7]


# ========================================================================
# 3. List Comprehension with if-else
# ========================================================================

# Syntax:
#     [value_if_true if condition else value_if_false for item in iterable]
#
# IMPORTANT:
#     With if-else, the condition comes BEFORE the for loop.

numbers = [1, 2, 3, 4, 5]

result = [
    "Even" if num % 2 == 0 else "Odd"
    for num in numbers
]

print(result)

# ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Another example: Convert negative numbers to zero.

numbers = [10, -5, 20, -3, 30]

result = [num if num > 0 else 0 for num in numbers]

print(result)

# [10, 0, 20, 0, 30]


# ========================================================================
# 4. List Comprehension with Strings
# ========================================================================

names = ["alice", "bob", "john"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)

# ['ALICE', 'BOB', 'JOHN']

# Extracting words with more than 3 characters

words = ["AI", "Python", "ML", "Engineering", "DL"]

long_words = [word for word in words if len(word) > 3]

print(long_words)

# ['Python', 'Engineering']


# ========================================================================
# 5. Nested List Comprehension
# ========================================================================

# A list comprehension can contain multiple for loops.
#
# Syntax:
#     [expression for outer_item in iterable1
#                 for inner_item in iterable2]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flattening a nested list

flattened = [
    num
    for row in matrix
    for num in row
]

print(flattened)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Explanation:
# First loop selects each row.
# Second loop selects each element from that row.


# ========================================================================
# Part 2: Dictionary Comprehension
# ========================================================================

# 1. What is Dictionary Comprehension?
#
# Dictionary comprehension creates a dictionary in one line.
#
# Syntax:
#     {key_expression: value_expression for item in iterable}
#
# It creates key-value pairs.

numbers = [1, 2, 3, 4, 5]

squares = {num: num ** 2 for num in numbers}

print(squares)

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ========================================================================
# 2. Dictionary Comprehension with Conditions
# ========================================================================

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(even_squares)

# {2: 4, 4: 16, 6: 36}


# ========================================================================
# 3. Creating a Dictionary from Two Lists
# ========================================================================

# zip() combines corresponding elements from two iterables.

names = ["Alice", "Bob", "John"]
ages = [22, 25, 28]

students = {
    name: age
    for name, age in zip(names, ages)
}

print(students)

# {'Alice': 22, 'Bob': 25, 'John': 28}


# ========================================================================
# 4. Dictionary Comprehension with if-else
# ========================================================================

numbers = [1, 2, 3, 4, 5]

result = {
    num: "Even" if num % 2 == 0 else "Odd"
    for num in numbers
}

print(result)

# {1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}


# ========================================================================
# 5. Reversing Keys and Values
# ========================================================================

student = {
    "Alice": 22,
    "Bob": 25,
    "John": 28
}

reversed_dict = {
    age: name
    for name, age in student.items()
}

print(reversed_dict)

# {22: 'Alice', 25: 'Bob', 28: 'John'}

# IMPORTANT:
# Dictionary keys must be unique.
# If duplicate keys are generated, the later value overwrites the earlier one.


# ========================================================================
# Part 3: Set Comprehension
# ========================================================================

# 1. What is Set Comprehension?
#
# Set comprehension creates a set in one line.
#
# Syntax:
#     {expression for item in iterable}
#
# Sets automatically remove duplicate values.

numbers = [1, 2, 2, 3, 3, 4, 5]

squares = {num ** 2 for num in numbers}

print(squares)

# {1, 4, 9, 16, 25}


# ========================================================================
# 2. Set Comprehension with Conditions
# ========================================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = {
    num
    for num in numbers
    if num % 2 == 0
}

print(even_numbers)

# {2, 4, 6, 8}


# ========================================================================
# 3. Difference Between List, Dictionary and Set Comprehension
# ========================================================================

numbers = [1, 2, 3, 4]

# List comprehension -> Uses square brackets.

list_result = [num ** 2 for num in numbers]

# Dictionary comprehension -> Uses key-value pairs and curly brackets.

dict_result = {num: num ** 2 for num in numbers}

# Set comprehension -> Uses curly brackets without key-value pairs.

set_result = {num ** 2 for num in numbers}

print(list_result)
print(dict_result)
print(set_result)

# List -> [1, 4, 9, 16]
# Dict -> {1: 1, 2: 4, 3: 9, 4: 16}
# Set  -> {16, 1, 4, 9}


# ========================================================================
# Part 4: sorted() Function
# ========================================================================

# 1. What is sorted()?
#
# sorted() sorts the elements of an iterable.
#
# Syntax:
#     sorted(iterable, key=None, reverse=False)
#
# iterable -> Mandatory. List, tuple, set, dictionary, etc.
# key      -> Optional. Function used to determine sorting order.
# reverse  -> Optional. False by default.
#
# Returns:
#     A NEW SORTED LIST.
#
# IMPORTANT:
#     sorted() is a built-in function, NOT a method.
#     Syntax: sorted(my_list)
#     NOT: my_list.sorted()


# ========================================================================
# 2. Sorting a List
# ========================================================================

numbers = [50, 10, 40, 20, 30]

# Ascending order (default)

result = sorted(numbers)

print(result)

# [10, 20, 30, 40, 50]

# Descending order

result = sorted(numbers, reverse=True)

print(result)

# [50, 40, 30, 20, 10]

# Original list remains unchanged.

print(numbers)

# [50, 10, 40, 20, 30]


# ========================================================================
# 3. Sorting Strings
# ========================================================================

names = ["John", "Alice", "Bob", "David"]

result = sorted(names)

print(result)

# ['Alice', 'Bob', 'David', 'John']

# Descending order

result = sorted(names, reverse=True)

print(result)


# ========================================================================
# 4. Sorting with key
# ========================================================================

# key specifies a function that determines how elements are sorted.
#
# Syntax:
#     sorted(iterable, key=function)
#
# The key function is applied to each element.
# Sorting happens based on the returned value.

names = ["John", "Alexander", "Bob", "Christopher"]

# Sort according to length of each name.

result = sorted(names, key=len)

print(result)

# ['Bob', 'John', 'Alexander', 'Christopher']

# Sort according to length in descending order.

result = sorted(names, key=len, reverse=True)

print(result)

# ['Christopher', 'Alexander', 'John', 'Bob']


# ========================================================================
# 5. Sorting Tuples Using key
# ========================================================================

students = [
    ("Alice", 85),
    ("Bob", 95),
    ("John", 75),
    ("David", 90)
]

# Each tuple contains:
#     Index 0 -> Name
#     Index 1 -> Marks

# Sort according to marks.

result = sorted(students, key=lambda x: x[1])

print(result)

# [('John', 75), ('Alice', 85), ('David', 90), ('Bob', 95)]

# Highest marks first.

result = sorted(students, key=lambda x: x[1], reverse=True)

print(result)

# [('Bob', 95), ('David', 90), ('Alice', 85), ('John', 75)]


# ========================================================================
# 6. Sorting Dictionaries
# ========================================================================

# By default, iterating over a dictionary gives its keys.

scores = {
    "Alice": 85,
    "Bob": 95,
    "John": 75
}

# Sort dictionary keys alphabetically.

result = sorted(scores)

print(result)

# ['Alice', 'Bob', 'John']

# Sort dictionary items by values.

result = sorted(scores.items(), key=lambda item: item[1])

print(result)

# [('John', 75), ('Alice', 85), ('Bob', 95)]

# Highest score first.

result = sorted(
    scores.items(),
    key=lambda item: item[1],
    reverse=True
)

print(result)

# [('Bob', 95), ('Alice', 85), ('John', 75)]


# ========================================================================
# Part 5: Lambda Functions
# ========================================================================

# 1. What is Lambda?
#
# A lambda is a small anonymous function.
#
# Anonymous means it does not need a function name.
#
# Syntax:
#     lambda arguments: expression
#
# Lambda can accept multiple arguments.
# Lambda contains only ONE expression.
# The expression result is returned automatically.
#
# No return keyword is required.


# ========================================================================
# 2. Normal Function vs Lambda
# ========================================================================

# Normal function

def square(num):
    return num ** 2

print(square(5))

# 25

# Same function using lambda

square = lambda num: num ** 2

print(square(5))

# 25


# ========================================================================
# 3. Lambda with Multiple Arguments
# ========================================================================

# Lambda can accept multiple arguments.

add = lambda a, b: a + b

print(add(10, 20))

# 30

multiply = lambda a, b: a * b

print(multiply(5, 4))

# 20

# Lambda with three arguments

calculate = lambda a, b, c: a + b + c

print(calculate(10, 20, 30))

# 60


# ========================================================================
# 4. Lambda with Conditions
# ========================================================================

# Lambda can use conditional expressions.

check_even = lambda num: "Even" if num % 2 == 0 else "Odd"

print(check_even(10))

# Even

print(check_even(7))

# Odd


# ========================================================================
# 5. Lambda with sorted()
# ========================================================================

# One of the most common uses of lambda is with sorted().
#
# key=lambda x: ...
#
# It tells sorted() which value to use for sorting.

students = [
    ("Alice", 85),
    ("Bob", 95),
    ("John", 75)
]

# Sort by marks.

result = sorted(students, key=lambda x: x[1])

print(result)

# [('John', 75), ('Alice', 85), ('Bob', 95)]

# Sort by name.

result = sorted(students, key=lambda x: x[0])

print(result)

# [('Alice', 85), ('Bob', 95), ('John', 75)]


# ========================================================================
# Part 6: enumerate() Function
# ========================================================================

# 1. What is enumerate()?
#
# enumerate() adds an index/counter to an iterable.
#
# Syntax:
#     enumerate(iterable, start=0)
#
# iterable -> Mandatory.
# start    -> Optional. Starting index (default: 0).
#
# Returns:
#     An enumerate iterator producing (index, value) pairs.


# ========================================================================
# 2. Using enumerate()
# ========================================================================

names = ["Alice", "Bob", "John"]

# Normal for loop

for i in range(len(names)):
    print(i, names[i])

# Using enumerate()

for index, name in enumerate(names):
    print(index, name)

# Output:
# 0 Alice
# 1 Bob
# 2 John


# ========================================================================
# 3. enumerate() with Custom Starting Index
# ========================================================================

names = ["Alice", "Bob", "John"]

for index, name in enumerate(names, start=1):
    print(index, name)

# Output:
# 1 Alice
# 2 Bob
# 3 John


# ========================================================================
# 4. Converting enumerate() into a List
# ========================================================================

names = ["Alice", "Bob", "John"]

result = list(enumerate(names))

print(result)

# [(0, 'Alice'), (1, 'Bob'), (2, 'John')]


# ========================================================================
# 5. enumerate() with List Comprehension
# ========================================================================

names = ["Alice", "Bob", "John"]

result = [
    (index, name)
    for index, name in enumerate(names, start=1)
]

print(result)

# [(1, 'Alice'), (2, 'Bob'), (3, 'John')]


# ========================================================================
# Part 7: zip() Function
# ========================================================================

# 1. What is zip()?
#
# zip() combines elements from two or more iterables.
#
# Syntax:
#     zip(iterable1, iterable2, ...)
#
# All iterables are mandatory.
#
# Returns:
#     A zip iterator producing tuples.
#
# IMPORTANT:
#     zip() stops when the SHORTEST iterable is exhausted.
#
#     It does not automatically fill missing values.


# ========================================================================
# 2. Using zip() with Two Lists
# ========================================================================

names = ["Alice", "Bob", "John"]

ages = [22, 25, 28]

result = zip(names, ages)

print(list(result))

# [('Alice', 22), ('Bob', 25), ('John', 28)]


# ========================================================================
# 3. Using zip() with Multiple Lists
# ========================================================================

names = ["Alice", "Bob", "John"]

ages = [22, 25, 28]

cities = ["Pune", "Mumbai", "Delhi"]

result = list(zip(names, ages, cities))

print(result)

# [
#     ('Alice', 22, 'Pune'),
#     ('Bob', 25, 'Mumbai'),
#     ('John', 28, 'Delhi')
# ]


# ========================================================================
# 4. zip() with Unequal Length Lists
# ========================================================================

names = ["Alice", "Bob", "John"]

ages = [22, 25]

result = list(zip(names, ages))

print(result)

# [('Alice', 22), ('Bob', 25)]

# John is excluded because ages has only two elements.


# ========================================================================
# 5. Looping Through zip()
# ========================================================================

names = ["Alice", "Bob", "John"]

ages = [22, 25, 28]

for name, age in zip(names, ages):
    print(name, age)

# Alice 22
# Bob 25
# John 28


# ========================================================================
# 6. zip() with Dictionary Comprehension
# ========================================================================

names = ["Alice", "Bob", "John"]

marks = [85, 95, 75]

students = {
    name: mark
    for name, mark in zip(names, marks)
}

print(students)

# {'Alice': 85, 'Bob': 95, 'John': 75}


# ========================================================================
# 7. Unzipping Using zip(*)
# ========================================================================

# The * operator unpacks an iterable.
# zip(*data) reverses the grouping done by zip().

data = [
    ("Alice", 22),
    ("Bob", 25),
    ("John", 28)
]

names, ages = zip(*data)

print(names)

# ('Alice', 'Bob', 'John')

print(ages)

# (22, 25, 28)


# ========================================================================
# Part 8: Nested Data - List of Dictionaries
# ========================================================================

# 1. What is Nested Data?
#
# Nested data means storing one data structure inside another.
#
# Example:
#     A list containing multiple dictionaries.
#
# This structure is very common in AI engineering.
#
# API responses, datasets and JSON data frequently use this format.


# ========================================================================
# 2. Creating a List of Dictionaries
# ========================================================================

students = [
    {
        "name": "Alice",
        "age": 22,
        "marks": 85
    },
    {
        "name": "Bob",
        "age": 25,
        "marks": 95
    },
    {
        "name": "John",
        "age": 28,
        "marks": 75
    }
]

print(students)


# ========================================================================
# 3. Accessing Nested Data
# ========================================================================

# Access the first dictionary.

print(students[0])

# Access a specific value.

print(students[0]["name"])

# Alice

print(students[1]["marks"])

# 95

# Access the second student's name.

print(students[1]["name"])

# Bob


# ========================================================================
# 4. Looping Through a List of Dictionaries
# ========================================================================

for student in students:
    print(student["name"], student["marks"])

# Alice 85
# Bob 95
# John 75


# ========================================================================
# 5. Adding Data to Nested Dictionaries
# ========================================================================

# Adding a new dictionary to the list.

students.append({
    "name": "David",
    "age": 24,
    "marks": 90
})

print(students)

# Adding a new key to an existing dictionary.

students[0]["city"] = "Pune"

print(students[0])


# ========================================================================
# 6. Updating Nested Dictionary Values
# ========================================================================

# Update Alice's marks.

students[0]["marks"] = 90

print(students[0])

# Update multiple values.

students[0].update({
    "age": 23,
    "city": "Mumbai"
})

print(students[0])


# ========================================================================
# 7. Filtering List of Dictionaries
# ========================================================================

students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 95},
    {"name": "John", "marks": 75},
    {"name": "David", "marks": 90}
]

# Get students who scored more than 80.

high_scorers = [
    student
    for student in students
    if student["marks"] > 80
]

print(high_scorers)

# [
#     {'name': 'Alice', 'marks': 85},
#     {'name': 'Bob', 'marks': 95},
#     {'name': 'David', 'marks': 90}
# ]


# ========================================================================
# 8. Sorting a List of Dictionaries
# ========================================================================

students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 95},
    {"name": "John", "marks": 75},
    {"name": "David", "marks": 90}
]

# Sort according to marks in ascending order.

result = sorted(
    students,
    key=lambda student: student["marks"]
)

print(result)

# Sort according to marks in descending order.

result = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True
)

print(result)

# Bob -> 95
# David -> 90
# Alice -> 85
# John -> 75


# ========================================================================
# 9. Extracting Specific Information
# ========================================================================

students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 95},
    {"name": "John", "marks": 75}
]

# Extract all names.

names = [student["name"] for student in students]

print(names)

# ['Alice', 'Bob', 'John']

# Extract all marks.

marks = [student["marks"] for student in students]

print(marks)

# [85, 95, 75]

# Extract names of students who scored above 80.

names = [
    student["name"]
    for student in students
    if student["marks"] > 80
]

print(names)

# ['Alice', 'Bob']


# ========================================================================
# Part 9: Practical AI Engineering Examples
# ========================================================================


# ------------------------------------------------------------------------
# 1. Processing AI Model Results
# ------------------------------------------------------------------------

# Model results are often stored as a list of dictionaries.

predictions = [
    {"label": "Cat", "confidence": 0.95},
    {"label": "Dog", "confidence": 0.80},
    {"label": "Bird", "confidence": 0.60},
    {"label": "Horse", "confidence": 0.90}
]

# Sort predictions by confidence.

sorted_predictions = sorted(
    predictions,
    key=lambda item: item["confidence"],
    reverse=True
)

print(sorted_predictions)

# Get the highest confidence prediction.

best_prediction = sorted_predictions[0]

print(best_prediction)

# {'label': 'Cat', 'confidence': 0.95}


# ------------------------------------------------------------------------
# 2. Filtering Model Predictions
# ------------------------------------------------------------------------

predictions = [
    {"label": "Cat", "confidence": 0.95},
    {"label": "Dog", "confidence": 0.80},
    {"label": "Bird", "confidence": 0.60}
]

# Keep predictions with confidence above 0.75.

filtered_predictions = [
    prediction
    for prediction in predictions
    if prediction["confidence"] > 0.75
]

print(filtered_predictions)


# ------------------------------------------------------------------------
# 3. Creating a Vocabulary from Text Data
# ------------------------------------------------------------------------

documents = [
    "Python is useful for AI",
    "AI is useful for ML",
    "Python is powerful"
]

# Extract all unique words.

vocabulary = {
    word.lower()
    for document in documents
    for word in document.split()
}

print(vocabulary)

# A set is useful because it automatically removes duplicate words.


# ------------------------------------------------------------------------
# 4. Processing Dataset Records
# ------------------------------------------------------------------------

dataset = [
    {"text": "  PYTHON IS USEFUL  ", "label": "positive"},
    {"text": "  AI IS POWERFUL  ", "label": "positive"},
    {"text": "  ML IS INTERESTING  ", "label": "positive"}
]

# Clean text using strip() and lower().

cleaned_dataset = [
    {
        "text": record["text"].strip().lower(),
        "label": record["label"]
    }
    for record in dataset
]

print(cleaned_dataset)


# ------------------------------------------------------------------------
# 5. Combining Dataset Columns
# ------------------------------------------------------------------------

names = ["Alice", "Bob", "John"]

scores = [85, 95, 75]

# Combine into a list of dictionaries.

dataset = [
    {"name": name, "score": score}
    for name, score in zip(names, scores)
]

print(dataset)

# [
#     {'name': 'Alice', 'score': 85},
#     {'name': 'Bob', 'score': 95},
#     {'name': 'John', 'score': 75}
# ]


# ========================================================================
# Part 10: Quick Revision
# ========================================================================

# LIST COMPREHENSION
#
# [expression for item in iterable]
# -> Creates and returns a NEW LIST; iterable is mandatory.
#
# [expression for item in iterable if condition]
# -> Creates a filtered NEW LIST; condition is optional.
#
# [value_if_true if condition else value_if_false for item in iterable]
# -> Creates a NEW LIST using if-else.


# DICTIONARY COMPREHENSION
#
# {key: value for item in iterable}
# -> Creates and returns a NEW DICTIONARY; iterable is mandatory.
#
# {key: value for item in iterable if condition}
# -> Creates a filtered NEW DICTIONARY; condition is optional.


# SET COMPREHENSION
#
# {expression for item in iterable}
# -> Creates and returns a NEW SET; iterable is mandatory.
#
# {expression for item in iterable if condition}
# -> Creates a filtered NEW SET; condition is optional.


# SORTED()
#
# sorted(iterable, key=None, reverse=False)
# -> Returns a NEW SORTED LIST; iterable mandatory, key and reverse optional.
# -> key is a function; reverse=True sorts in descending order.
#
# Example:
# sorted(students, key=lambda x: x["marks"], reverse=True)


# LAMBDA
#
# lambda arguments: expression
# -> Creates and returns a function; arguments depend on the operation.
# -> No explicit return keyword; expression result is returned automatically.
#
# Example:
# lambda x: x ** 2
# lambda a, b: a + b
# lambda x: x[1]


# ENUMERATE()
#
# enumerate(iterable, start=0)
# -> Returns an enumerate iterator of (index, value) pairs.
# -> iterable mandatory; start optional (default: 0).
#
# Example:
# enumerate(names)
# enumerate(names, start=1)


# ZIP()
#
# zip(iterable1, iterable2, ...)
# -> Returns a zip iterator of tuples; at least one iterable is required.
# -> Combines corresponding elements and stops at the shortest iterable.
#
# Example:
# zip(names, ages)
# list(zip(names, ages))
# zip(*data) -> Unpacks grouped elements.


# NESTED DATA: LIST OF DICTIONARIES
#
# students[0]
# -> Returns the first dictionary from the list.
#
# students[0]["name"]
# -> Returns the name value from the first dictionary.
#
# students.append(dictionary)
# -> Adds a dictionary to the list; dictionary mandatory; returns None.
#
# students[0].update(dictionary)
# -> Updates the first dictionary; dictionary mandatory; returns None.
#
# [student["name"] for student in students]
# -> Returns a NEW LIST containing all student names.
#
# sorted(students, key=lambda student: student["marks"])
# -> Returns a NEW LIST sorted by marks.


# ========================================================================
# END OF COMPREHENSIONS, LAMBDA, ENUMERATE, ZIP AND NESTED DATA
# ========================================================================