num = int(input("Enter a number: "))
for i in range(1, num+1): print("FizzBuzz" if i%3==0 and i%5==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i)

## SECOND METHOD
# num = int(input("Enter a number : "))
# for i in range(1,num+1):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)