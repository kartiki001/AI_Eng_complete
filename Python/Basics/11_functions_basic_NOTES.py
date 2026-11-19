# =======================================================
# 1. functions
# =======================================================

def function_name():
    # Code to execute
    print("Hello Python")

function_name()

# Let's understand each part:
#     def- Keyword used to define a function.
#     function_name - Name of the function.
#     () - Parentheses where parameters can be placed.
#     : - Indicates the beginning of the function body.
#     Indented code - Instructions inside the function.
#     function_name() - Function call that executes the function.



# =======================================================
# 2. Parameters and Arguments
# =======================================================

# Parameters are variables written inside the function definition.
# Arguments are actual values passed when calling the function.


def greet(name):  # name is a parameter
    print("Hello", name)

greet("Rahul")    # Rahul is an argument


# =======================================================
# 3. Default Arguments
# =======================================================


# A default argument is a value automatically used when the caller does not provide an argument for that parameter.

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Rahul")

# Hello Student
# Hello Rahul

### Important rule: Parameters with default values must come after parameters without default values.
# correct - def student(name, age=18):
# incorrect - def student(name="Rahul", age):   ---> SYNTAX ERROR


# =======================================================
# positional argument passing.-->
def student(name, age, course):
    print(name, age, course)
student("Rahul", 22, "Python")

# keyword arguments.-->
def student(name, age, course):
    print(name, age, course)
student(age=22, course="Python", name="Rahul")


# Positional arguments must come before keyword arguments.
def student(name, age, course):
    print(name, age, course)
student("Rahul", age=22, course="AI")

# =======================================================
# 5. Return Values
# =======================================================
# A function can perform a calculation and send its result back to the place where it was called.
# We use the return keyword for this.

def add(a, b):
    return a + b
result = add(10, 20)
print(result)

# Let's understand what happened:
    # add(10, 20) calls the function.
    # Python calculates 10 + 20.
    # return sends the result 30 back.
    # The result is stored in the result variable.
    # print(result) displays 30.

### IMPORTANT --
# print()  -  Displays information on the screen.
# return  -  Sends a value back to the caller.

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication

result = calculate(10, 5)
print(result)

# output -> tuple - (15, 5, 50)

# unpack the value --
add, sub, mul = calculate(10, 5)
print(add)
print(sub)
print(mul)


# =======================================================
# 6. Scope of Variables
# =======================================================

# Scope determines where a variable can be accessed in your Python program.

# There are two important types to understand initially:
    # Local scope.
    # Global scope.

def greet():
    message = "Hello Python"
greet()
print(message)

# output -> NameError as messgae is local variable

name = "Rahul"

def greet():
    print(name)

greet()
print(name)

# output -> as name is global variable
# Rahul
# Rahul


# GLOBAL KEYWORD:
def update_count():
    global count
    count = 20

# Enclosing scope:
def outer():
    message = "Hello"
    def inner():
        print(message)
    inner()
outer()

# nonlocal ->  to modify a variable in an enclosing function.
def outer():
    count = 10
    def inner():
        nonlocal count
        count = 20
    inner()
    print(count)
outer()

# =======================================================
# 7. Docstring
# =======================================================

# A docstring is a string used to explain what a function, class, or module does.
# It is written immediately after the function definition.

def add(a, b):
    """
    This function adds two numbers.

    Parameters:
        a: First number
        b: Second number

    Returns:
        Sum of a and b.
    """
    return a + b

# Why are docstrings useful?
    # They explain what your function does.
    # They describe parameters and return values.
    # They help other developers understand your code.
    # Documentation tools can read them.
    # They are especially useful when building large AI applications.


# Accessing a docstring
# You can access a function's docstring using .__doc__.

def greet(name):
    """Greets the user by name."""
    print("Hello", name)

print(greet.__doc__)
# or you can also use
help(greet)

# ============================================================
# PYTHON FUNCTIONS - COMPLETE SUMMARY
# ============================================================
#
# Concept             | Meaning                          | Example
# --------------------|----------------------------------|-------------------------
# def                 | Defines a function               | def greet():
# Parameter           | Variable in function definition  | def greet(name):
# Argument            | Value passed to function         | greet("Rahul")
# Default Argument    | Parameter with default value     | age=18
# Keyword Argument    | Argument passed by name          | name="Rahul"
# return              | Sends result back to caller      | return a + b
# Local Scope         | Variable inside a function       | x = 10 (inside function)
# Global Scope        | Variable outside a function      | x = 10 (module level)
# Docstring           | Function documentation           | """Add numbers."""
#
# ============================================================