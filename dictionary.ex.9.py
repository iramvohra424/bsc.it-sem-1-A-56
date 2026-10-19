# Exercise 9: Mini Phone Book (Functions)
# Write four functions:
# add(name, number) uses update().
# search(name) uses get() and prints "Not found" if missing.
# delete(name) uses pop() with a default and handles missing contacts.
# show() prints contacts alphabetically using items().
# Call the functions in the order specified in the question.

contacts = {}

def add(name, number):
    contacts.update({name: number})
    print("Saved", name)

def search(name):
    number = contacts.get(name, "Not found")
    print(name + ":", number)

def delete(name):
    number = contacts.pop(name, None)

    if number is None:
        print(name, "does not exist")
    else:
        print("Deleted", name)

def show():
    for name, number in sorted(contacts.items()):
        print("  " + name.ljust(10), number)

add("Kiran", "99090 12345")
add("Meet", "98980 54321")
add("Kiran", "99090 00000")
search("Kiran")
search("Riya")
delete("Meet")
delete("Meet")
add("Hetal", "97370 11223")
show()