#49. password until correct password is entered

password="1234"

p=input("enter password: ")

while p!=password:
    print("incorrect password")
    p=input("enter password: ")

print("correct password")