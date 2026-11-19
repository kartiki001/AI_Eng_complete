def max_of_three(a,b,c):
    return max(a,b,c)

x,y,z = map(int,input("Enter 3 numbers : ").split())
print(max_of_three(x,y,z))