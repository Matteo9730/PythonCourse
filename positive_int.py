#Using tail recursion, perform the calculation of the sum of the first n positive integers
import functools 

@functools.lru_cache(maxsize= None) 
def sum(n, accumulator=0):
    if n<1: 
        return accumulator
    else:
        return sum(n-1, n+accumulator)

res= sum(6)
print(res)