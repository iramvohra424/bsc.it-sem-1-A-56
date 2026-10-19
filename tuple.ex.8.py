# 8. Find the length of each city name with and without len().

cities = ("Ahmedabad", "Surat", "Rajkot", "Vadodara")

for city in cities:
    print(city, "Length using len():", len(city))

    count = 0
    for ch in city:
        count += 1

    print(city, "Length without len():", count)