# 29. Remove None or empty values from a list.

values = [10, None, "", 20, None, 30, ""]
result = []

for value in values:
    if value is not None and value != "":
        result.append(value)

print(result)