# 3. Find the total marks using sum() and without using sum().

t2 = (78, 85, 69, 90, 82)

print("Total using sum():", sum(t2))

total = 0
for marks in t2:
    total += marks

print("Total without sum():", total)