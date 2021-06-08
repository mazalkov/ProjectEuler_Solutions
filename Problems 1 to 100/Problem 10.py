# https://projecteuler.net/problem=10


def eratosthenes(n):

    multiples = set()

    for i in range(2, n+1):

        if i not in multiples:

            yield i

            multiples.update(range(i*i, n+1, i))


iter = 0
ml = list(eratosthenes(2000000))
for x in ml:
    iter = int(x) + iter

print(iter)
# 142913828922
