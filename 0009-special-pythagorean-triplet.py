n = 1000 + 1
product = 0
found = False
for a in range(1, n):
    for b in range(1, n):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            found = True
            product = a*b*c
            break
    if found:
        break

print(product)
