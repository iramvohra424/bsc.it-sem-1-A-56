# 14. Check whether a string contains any vowel, count each vowel, and find the total vowels.

s = input("Enter a string: ").lower()

a = s.count('a')
e = s.count('e')
i = s.count('i')
o = s.count('o')
u = s.count('u')

total = a + e + i + o + u

if total > 0:
    print("Vowels are present")
else:
    print("No vowels are present")

print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)
print("Total vowels:", total)