def get_next_prime(arr, prime):
    for k in range(prime + 1, len(arr)):
        if arr[k] == 0:
            return k

def prime_sieve(n):
    arr = [0] * n
    arr[0] = 1
    arr[1] = 1
    prime = 2
    while prime**2 < n:
        for j in range(prime**2, n, prime):
            arr[j] = 1
        prime = get_next_prime(arr, prime)
    return arr

prime_sum = 0
prime_arr = prime_sieve(2000000)
for i, item in enumerate(prime_arr):
    if item == 0:
        prime_sum += i

print(prime_sum)
