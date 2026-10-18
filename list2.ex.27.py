# 27. Check whether a list is a palindrome.

numbers = [1, 2, 3, 2, 1]

if numbers == numbers[::-1]:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")