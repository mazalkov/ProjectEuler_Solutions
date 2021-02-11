# https://projecteuler.net/problem=4


# very inefficient and needs much improvement
arr = []

for i in range(100, 1000):
    for j in range(100, 1000):
        if (str(i*j) == str(i*j)[::-1]):
            arr.append(i*j)
            
       
print(max(arr))
