# 61. Check whether a list is a palindrome without converting it to a string.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
is_palindrome = True

for i in range(len(numbers) // 2):
    if numbers[i] != numbers[len(numbers) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")