#7.smallest number
a=int(input("enter thr first number :"))
b=int(input("enter thr second number :"))
c=int(input("enter thr third number :"))
if a<b and a<c:
    print("smallest",a)
elif b<c:
    print("smallest",b)
else:
    print("smallest",c)
