#57. reverse a string

s=input("enter a string: ")

rev=""
for i in s:
    rev=i+rev

print("reverse string = ",rev)