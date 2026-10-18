#46. password and number input using while loop

password="1234"
while True:
    p=input("enter password: ")
    if p==password:
        print("correct password")
        break
    else:
        print("incorrect password")

n=int(input("enter a number: "))
while n!=0:
    n=int(input("enter a number: "))
print("you entered 0")