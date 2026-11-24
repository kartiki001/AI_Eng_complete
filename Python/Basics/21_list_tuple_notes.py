# ========================================================================
# Part 1: Python Lists
# ========================================================================

# 1. What is a list?
#     A list is an ordered, mutable collection of elements.
#     Ordered: Elements maintain their insertion order.
#     Mutable: You can modify, add, or remove elements.
#     Allows duplicates: The same element can appear multiple times.
#     Heterogeneous: You can store different data types together.

numbers = [10, 20, 30, 40]
names = ["John", "Alice", "Bob"]
mixed = [10, "Python", 3.14, True]
duplicates = [10, 20, 10, 30]
#create list: 
my_list = []
# Another way
my_list = list()

# ========================================================================
# 2. Indexing in lists
# ========================================================================

# Indexing means accessing an element using its position.

numbers = [10, 20, 30, 40, 50]

print(numbers[0])  # 10
print(numbers[1])  # 20
print(numbers[2])  # 30
print(numbers[3])  # 40

# NEGATIVE INDEXING
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])  # 50
print(numbers[-2])  # 40
print(numbers[-3])  # 30

# ========================================================================
# 4. Slicing in lists
# ========================================================================

#syntax : list[start:end:step]
    # start: Starting index (included).
    # end: Ending index (excluded).
    # step: How many positions to skip.

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:3]) # [10, 20, 30]
print(numbers[2:5]) # [30, 40, 50]
print(numbers[:3]) # [10, 20, 30]
print(numbers[3:]) # [40, 50, 60] 
print(numbers[:]) # Entire list

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[::2]) # [10, 30, 50]
print(numbers[::3]) # [10, 40]
print(numbers[::-1]) # [60, 50, 40, 30, 20, 10]

training_data = list(range(1000))
batch = training_data[0:100]
print(len(batch)) # 100

# ========================================================================
# Part 2: Important List Methods
# ========================================================================

# append() adds one element at the end of a list.   ls.append(number ) - number added at last in list 
# extend() adds individual elements from another iterable.      ls.extend(ls2) - elemts of ls2 added in ls1 - output is single list
# insert() adds an element at a specific position.  list.insert(index, element)
# remove() removes the first matching value from a list.    ls.remove(x) - first x from ls is removed
# pop() removes an element and returns the removed element. By default, pop() removes the last element. You can also specify an index: r=ls.pop(2)

## REMOVE - REMOVES BY VALUE
## POP - REMOVES BY INDEX

# ls.sort()     ls.sort(reverse=True)

results = [
    ("AI", 0.85),
    ("ML", 0.95),
    ("DL", 0.75)
]
results.sort(key=lambda x: x[1], reverse=True)
print(results)

# len() returns the number of elements in a list.
# The in operator checks whether an element exists in a list. It returns a Boolean: True or False.
# You can also use not in.

numbers = [10, 20, 30, 40]
print(20 in numbers)

# loop in list
numbers = [10, 20, 30, 40]
for num in numbers:
    print(num)

numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    print(i, numbers[i])


names = ["John", "Alice", "Bob"]
for index, name in enumerate(names):
    print(index, name)
# 0 John
# 1 Alice
# 2 Bob

# List comprehension with conditions
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
# [2, 4, 6]



# ========================================================================
# Python Tuples
# ========================================================================

# A tuple is an ordered, immutable collection of elements.

# The main difference:
#     List: Mutable.
#     Tuple: Immutable.

# Tuples:
#     Maintain insertion order.
#     Allow duplicate values.
#     Support different data types.
#     Support indexing and slicing.
#     Cannot be modified after creation.

# CREATING TUPLE:
a = (10, 20, 30)
b = 10, 20, 30 # Without parentheses
c = () # Empty tuple
d = (10,) # Single-element tuple

a = (10) # <class 'int'>

# TUPLE SUPPORT INDEXING, NEGATIVE INDEXING AND SLICING.