max_product, max_i, max_j = 0, 0, 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j
        if product < max_product:
            break
        if str(product) == str(product)[::-1] and max_product < product:
                max_product = product
                max_i = i
                max_j = j
print(max_product)
