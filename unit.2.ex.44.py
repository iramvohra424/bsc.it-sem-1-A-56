#44. count vowels in a word

word=input("enter a word: ")

count=0
for i in word:
    if i in "aeiouAEIOU":
        count=count+1

print("number of vowels = ",count)