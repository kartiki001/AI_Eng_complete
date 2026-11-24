l1 = [1,4,4,6,8,9,15,22,60]
l2 = [2,4,8,11,15,20,30,35,40,55,60]
i = j = 0
result = []

while i < len(l1) and j < len(l2):
    if l1[i] <= l2[j]:
        result.append(l1[i])
        i += 1
    else:
        result.append(l2[j])
        j += 1

result.extend(l1[i:])
result.extend(l2[j:])

print(result)