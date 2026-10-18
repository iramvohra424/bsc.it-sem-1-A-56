#13. gross salary calculation

basic=int(input("enter basic pay: "))

if basic<5000:
    da=basic*30/100
else:
    da=basic*45/100

hra=basic*15/100
pf=basic*12/100

gross=basic+da+hra-pf

print("DA = ",da)
print("HRA = ",hra)
print("PF = ",pf)
print("Gross Salary = ",gross)