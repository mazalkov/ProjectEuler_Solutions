// https://projecteuler.net/problem=6
  
  
def sum_of_squares(n):
    return((1/6) * n * (n+1) * (2*n+1))
    
    
def square_of_sum(n):
    return(((1/2) * n * (n+1))**2)
    
    
    
print(int(square_of_sum(100) - sum_of_squares(100)))
# 25164150
