# 9. Create a nested tuple t4 containing name, hobbies, friends, and degree using inputs.

name = input("Enter name: ")

hobbies = input("Enter hobbies separated by commas: ").split(",")
friends = input("Enter friends separated by commas: ").split(",")
degree = input("Enter degree: ")

t4 = (name, tuple(hobbies), tuple(friends), degree)
print(t4)