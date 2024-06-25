#write a program that generates a random number between 1 and 100

import random 

def random_number():
    tot=random.randrange(1,101)
    return tot

print(random_number())