#Ask the user for a number, then use a loop to print its multiplication table from 1 to 10.
n= int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print (f"'{n}*{i} = {n*i}'")