#25. grade calculation

m1=int(input("enter first marks: "))
m2=int(input("enter second marks: "))
m3=int(input("enter third marks: "))

total=m1+m2+m3

print("total = ",total)

if total>=270:
    print("grade A")
elif total>=240:
    print("grade B")
elif total>=210:
    print("grade C")
elif total>=180:
    print("grade D")
else:
    print("fail")