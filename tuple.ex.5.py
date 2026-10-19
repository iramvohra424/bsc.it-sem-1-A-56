# 5. Input a number and check whether it is present as an element in t3.

t1 = ("Iram", "Khan", "Vohra")
t2 = (78, 85, 69, 90, 82)
t3 = (t1, t2)

n = int(input("Enter a number: "))

if n in t3[1]:
    print("Number is present")
else:
    print("Number is not present")