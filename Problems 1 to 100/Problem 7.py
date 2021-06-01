# https://projecteuler.net/problem=7


def list_of_primes(num_primes):
    
    primes = [2] # first known prime
    attempt = 3 # next integer to test
    
    while len(primes) < num_primes:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
        
    print(primes[-1])
    # returns 104743 when called with 10001
