import math

def get_next_prime(primes):
    num = primes[-1] + 1
    while True:
        found = True
        for i in range(len(primes)):
            if num % primes[i] == 0:
                found = False
                break
            if primes[i] > math.sqrt(num):
                break
        if found:
            break
        else:
            num += 1
    primes.append(num)

def get_nth_prime(n):
    primes = [2]
    count = 1
    while count < n:
        get_next_prime(primes)
        count += 1
    return primes[n-1]

print(get_nth_prime(10001))
