# 7. Create a tuple containing city names of Gujarat entered by the user.

cities = []

n = int(input("How many cities do you want to enter? "))

for i in range(n):
    city = input("Enter city name: ")
    cities.append(city)

t = tuple(cities)
print(t)