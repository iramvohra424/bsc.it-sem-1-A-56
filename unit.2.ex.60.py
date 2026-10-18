#60. check whether a number is an Armstrong number

n=int(input("enter a number: "))

temp=n
sum=0
digits=len(str(n))

while n>0:
    r=n%10
    sum=sum+r**digits
    n=n//10

if temp==sum:
    print("Armstrong number")
else:
    print("not an Armstrong number")