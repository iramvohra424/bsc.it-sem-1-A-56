for i in range(5, 0, -1):
    for j in range(i):
        if i == 5 or j == 0 or j == i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()