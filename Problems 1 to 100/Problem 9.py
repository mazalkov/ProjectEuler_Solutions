# https://projecteuler.net/problem=9


for a in range(1, 1000):
    b = a + 1
    c = b + 1
    
    while c <= 1000:
        while c**2 < (a**2 + b**2):
            c += 1
            
        if c**2 == (a**2 + b**2) and (c <= 1000) and (a + b + c == 1000):
                print(a*b*c)
                break
            
        b += 1
# 31875000
