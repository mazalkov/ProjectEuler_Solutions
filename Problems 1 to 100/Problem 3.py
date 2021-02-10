# https://projecteuler.net/problem=3


n = 600851475143

i = 2

while i*i <= n:
    
    if n % i:
        i += 1
        
    else:
        n //= i

        
print(n)
# 6857
