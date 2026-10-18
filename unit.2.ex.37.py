#37. print odd numbers from 1 to n using for and while loop

n=int(input("enter the number: "))

print("using for loop:")
for i in range(1,n+1):
    if i%2!=0:
        print(i)

print("using while loop:")
i=1
while i<=n:
    if i%2!=0:
        print(i)
    i=i+1