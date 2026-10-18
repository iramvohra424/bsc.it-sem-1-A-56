#45. count how many times the letter a occurs in a string

s=input("enter a string: ")

count=0
for i in s:
    if i=="a" or i=="A":
        count=count+1

print("number of times a occurs = ",count)