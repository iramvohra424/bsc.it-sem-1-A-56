#58. check whether a number is palindrome or not

n=int(input("enter a number: "))

temp=n
rev=0

while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10

if temp==rev:
    print("palindrome number")
else:
    print("not a palindrome number")