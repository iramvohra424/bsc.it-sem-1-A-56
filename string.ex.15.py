# 15. Copy the input string by replacing every 'o' with '@' without using replace().

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch == 'o':
        result += '@'
    else:
        result += ch

print(result)