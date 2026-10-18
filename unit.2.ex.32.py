#32. simple ATM menu

balance=1000

print("1. balance")
print("2. deposit")
print("3. withdrawal")

choice=int(input("enter your choice: "))

if choice==1:
    print("balance = ",balance)
elif choice==2:
    amount=int(input("enter deposit amount: "))
    balance=balance+amount
    print("updated balance = ",balance)
elif choice==3:
    amount=int(input("enter withdrawal amount: "))
    if amount<=balance:
        balance=balance-amount
        print("remaining balance = ",balance)
    else:
        print("insufficient balance")
else:
    print("invalid choice")