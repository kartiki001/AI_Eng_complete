def fib(n):
    a,b=1,1
    print(a)
    while b<=n:
        print(b)
        a,b = b, a+b

n = int(input("Enter a number: "))
fib(n)