#write a program that mixes a list of elements

import random 

def mix(x):
    random.shuffle(x) 
    return x
elements= ["a", "b", "c", 4]
print(mix(elements))