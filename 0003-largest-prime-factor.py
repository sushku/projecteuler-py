def is_prime(p, primes):
    for i in primes:
        if p % i == 0:
            return False
    return True

def get_next_prime(p, primes):
    p += 1

    while True:
        if is_prime(p, primes):
            break
        else:
            p += 1

    primes.append(p)
    return p

dividend = 600851475143
curr_prime = 2
primes = [2]
while dividend > 1:
    if dividend % curr_prime == 0:
        dividend /= curr_prime
    else:
        curr_prime = get_next_prime(curr_prime, primes)
print(curr_prime)
