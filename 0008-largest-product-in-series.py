from functools import reduce

with open('0008-input.txt', 'r') as f:
    num_str = f.read()

max_product = 0
for i in range(len(num_str) - 13):
    part_arr = list(num_str[i:i+13])
    product = reduce(lambda x, y: int(x) * int(y), part_arr)
    if product > max_product:
        max_product = product

print(max_product)
