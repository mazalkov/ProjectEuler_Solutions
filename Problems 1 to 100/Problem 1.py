# https://projecteuler.net/problem=1


multiples = []

for i in range(1, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        multiples.append(i)
        
print(sum(multiples))
# 233168
