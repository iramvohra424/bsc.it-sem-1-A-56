#47. menu-driven program until user selects Exit

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")

    choice=int(input("enter your choice: "))

    if choice==1:
        a=int(input("enter first number: "))
        b=int(input("enter second number: "))
        print("result = ",a+b)
    elif choice==2:
        a=int(input("enter first number: "))
        b=int(input("enter second number: "))
        print("result = ",a-b)
    elif choice==3:
        a=int(input("enter first number: "))
        b=int(input("enter second number: "))
        print("result = ",a*b)
    elif choice==4:
        print("exit")
        break
    else:
        print("invalid choice")