# 16. Create a tuple of strings and print each string in reverse order.
# Example: ('Pen', 'Marker', 'Pencil', 'Eraser', 'Scale')

t = ('Pen', 'Marker', 'Pencil', 'Eraser', 'Scale')
result = ()

for s in t:
    result += (s[::-1],)

print(result)