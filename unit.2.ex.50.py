#50. number guessing game

number=7

guess=int(input("guess the number: "))

while guess!=number:
    print("wrong guess")
    guess=int(input("guess the number: "))

print("correct guess")