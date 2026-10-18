#14. electricity bill calculation

units=int(input("enter units consumed: "))

if units<=50:
    bill=units*2.30
elif units<=100:
    bill=50*2.30+(units-50)*2.60
elif units<=300:
    bill=50*2.30+50*2.60+(units-100)*3.25
else:
    bill=50*2.30+50*2.60+150*3.25+(units-250)*4.35

print("Electricity Bill = Rs.",bill)