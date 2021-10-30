sequence = [1, 2, 3, 4, 5, 6, 7, 8]

doubled = [(lambda x: x*2)(x) for x in sequence]
doubled2 = [x*2 for x in sequence]

print(doubled)
print(doubled2)
print(sequence[:3])
