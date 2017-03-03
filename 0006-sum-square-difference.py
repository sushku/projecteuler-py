n = 100
sum = n * (n + 1) // 2
sq_of_sum = sum ** 2
sum_of_sq = 0
for i in range(1, n + 1):
    sum_of_sq += i ** 2
print(sq_of_sum - sum_of_sq)
