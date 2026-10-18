#11. simple calculator

a=int(input("enter first number: "))
b=int(input("enter second number: "))
op=input("enter operator (+, -, *, /): ")

if op=="+":
    print("result = ",a+b)
elif op=="-":
    print("result = ",a-b)
elif op=="*":
    print("result = ",a*b)
elif op=="/":
    if b!=0:
        print("result = ",a/b)
    else:
        print("division by zero is not possible")
else:
    print("invalid operator")