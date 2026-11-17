conversion_type = input("""What conversion you want - select option
    A: celcius to farhenite?
    B: farhenite to celcius\n""")

if (conversion_type.upper() == 'A'):
    celcius = int(input("Enter celcius temperature: "))
    farhenite = celcius * (9/5) + 32
    print (f"{celcius} converted to Farhenite is : {farhenite}")
else:
    farhenite = int(input("Enter farhenite temperature: "))
    celcius = (farhenite - 32) * 5/9
    print (f"{farhenite} converted to Farhenite is : {celcius}")
