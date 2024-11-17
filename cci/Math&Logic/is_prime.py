import math

def is_prime(number):
    if number <= 1:
        return False
    
    if number <= 3:
        return True
    
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(number)), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
        
    return True

# Sieve of Eratosthenes

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False

    p = 2
    while p * p <= n:
        if primes[p]:
            for multiple in range(p * p, n + 1, p):
                primes[multiple] = False
        p += 1

    return [i for i in range(n+1) if primes[i]]