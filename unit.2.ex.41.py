#41. sum of numbers from 1 to n using for and while loop

n=int(input("enter the number: "))

sum=0
print("using for loop:")
for i in range(1,n+1):
    sum=sum+i
print("sum = ",sum)

sum=0
i=1
print("using while loop:")
while i<=n:
    sum=sum+i
    i=i+1
print("sum = ",sum)