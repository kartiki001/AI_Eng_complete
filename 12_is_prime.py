def is_primary(num):
    d = 0
    for i in range(2, num//2):
        if num%i==0:
            d=1
            break
    return 'PRIME' if d == 0 else 'NOT PRIME'

num = int(input("ENTER A NUMBER: "))
a = is_primary(num)
print(a)