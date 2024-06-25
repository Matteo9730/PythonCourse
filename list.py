#write a prgram that lists all files in a specific directory

import os 

def lists(x):
    res= [f for f in os.listdir(x) if os.path.isfile(os.path.join(x, f))] #create a list with all files
    return res

path= os.fspath("<name.path>")
print(lists(path))