stud = [
    {
        'name' : 'Anurag',
        'age' : 20,
        'marks' : 78
    },
    {
        'name' : 'Yash',
        'age' : 87,
        'marks' : 87
    },
    {
        'name' : 'Tara',
        'age' : 85,
        'marks' : 44
    },
    {
        'name' : 'Ajay',
        'age' : 51,
        'marks' : 98
    }
]

result = sorted(stud, key=lambda x: x['marks'], reverse= True)
print(result)