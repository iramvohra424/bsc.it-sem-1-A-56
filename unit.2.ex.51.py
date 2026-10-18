#51. print numbers from 1 to 50 but skip multiples of 5

for i in range(1,51):
    if i%5==0:
        continue
    print(i)