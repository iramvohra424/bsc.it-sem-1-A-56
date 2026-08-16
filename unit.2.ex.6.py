#6.largest number among three numbers
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))

if a>b and a>c:
    print("largest= ",a)
elif b>c:
    print("largest= ",b)
else:
    print("largest= ",c)
