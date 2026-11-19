def factorial(f):
    fact = 1
    for i in range(1,f+1):
        fact *= i
    return fact

def recursive_factorial(f):
    if f>0:
        return f*recursive_factorial(f-1) 
    else:
        return 1

n = int(input("Enter a number : "))
print(factorial(n))
print(recursive_factorial(n))