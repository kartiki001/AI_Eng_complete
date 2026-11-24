l1 = [1,3,6,2,1,5,9,7,4,2,1,6,4,8,9,0,1,5,4,3,2,6,8,9,1]
# print(list(set(l1)))
res = []
for i in l1:
    if i not in res:
        res.append(i)
print(res)