#31. grade calculation

m1=int(input("enter first marks: "))
m2=int(input("enter second marks: "))
m3=int(input("enter third marks: "))

total=m1+m2+m3
percentage=total/3

print("total = ",total)
print("percentage = ",percentage)

if percentage>=80:
    print("grade A+")
elif percentage>=70:
    print("grade A")
elif percentage>=60:
    print("grade A-")
elif percentage>=50:
    print("grade B+")
elif percentage>=40:
    print("grade B")
else:
    print("fail")