para = '''AI ML, AI ML, DS GCP, Azure, lawrence hence lawrence'''
para = para.replace(", ", " ")
para = para.replace(". ", " ")

l1 = para.split()
result = {}
for i in l1:
    if i in result:
        result[i]+=1
    else:
        result.update({i:1})
print(result)