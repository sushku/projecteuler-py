import functools

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

def divide(divs, factor):
    divided = False
    for i in range(len(divs)):
        if divs[i] % factor == 0:
            divs[i] //= factor
            divided = True
    return divided

num = 20
divisors = list(range(num + 1))[1:]
factors = []
prime = 2
primes = [prime]
while divisors.count(1) < num:
    if divide(divisors, prime):
        factors.append(prime)
    else:
        prime = get_next_prime(prime, primes)

print(functools.reduce(lambda x,y: x*y, factors))
