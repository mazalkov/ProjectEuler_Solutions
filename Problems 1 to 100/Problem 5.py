# https://projecteuler.net/problem=5


i = 2520

while True:
    if all((i % j == 0) for j in range(11, 21)):
        break
    else:
        i += 2520

print(i)
# 232792560
