#65. find the LCM of two numbers

a=int(input("enter first number: "))
b=int(input("enter second number: "))

if a>b:
    max=a
else:
    max=b

while True:
    if max%a==0 and max%b==0:
        print("LCM = ",max)
        break
    max=max+1