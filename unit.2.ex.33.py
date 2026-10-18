#33. positive and even or odd

n=int(input("enter a number: "))

if n>0:
    print("positive")
    if n%2==0:
        print("even")
    else:
        print("odd")
else:
    print("number is not positive")