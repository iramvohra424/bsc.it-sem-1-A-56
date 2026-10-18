#59. check whether a string is palindrome or not

s=input("enter a string: ")

rev=""
for i in s:
    rev=i+rev

if s==rev:
    print("palindrome string")
else:
    print("not a palindrome string")