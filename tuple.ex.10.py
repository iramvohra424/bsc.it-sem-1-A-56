# 10. Find an element in nested tuple t4 and print its position if found;
# otherwise, display "Not found".

t4 = ("Aadil", ("Reading", "Cricket"), ("Rahul", "Aman"), "BCA")
element = input("Enter an element to search: ")

found = False

for i in range(len(t4)):
    if isinstance(t4[i], tuple):
        if element in t4[i]:
            print("Position:", i, t4[i].index(element))
            found = True
    elif element == t4[i]:
        print("Position:", i)
        found = True

if not found:
    print("Not found")