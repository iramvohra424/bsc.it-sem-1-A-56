#52. sum of 10 numbers skipping negative numbers

sum=0

for i in range(1,11):
    n=int(input("enter a number: "))
    if n<0:
        continue
    sum=sum+n

print("sum = ",sum)