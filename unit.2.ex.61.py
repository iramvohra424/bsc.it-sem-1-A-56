#61. check whether a number is prime

n=int(input("enter a number: "))

if n<=1:
    print("not a prime number")
else:
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1

    if count==2:
        print("prime number")
    else:
        print("not a prime number")