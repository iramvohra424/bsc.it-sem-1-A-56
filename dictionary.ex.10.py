# Exercise 10: Predict the Output
# Predict the output of each statement involving get(), update(), pop(),
# keys(), values(), and dictionary membership. Then run the program
# to check your answers.

d = {"a": 1, "b": 2}

print(d.get("c"))
print(d.get("a", 100))

x = d.update({"b": 20, "c": 3})
print(x, d)

print(d.pop("a"), d)

print(len(d.keys()) + sum(d.values()))

k = d.keys()
d["z"] = 26
print(list(k))

print("b" in d, 20 in d)