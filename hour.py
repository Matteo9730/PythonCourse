#write a program that prints out the current date and time

from datetime import datetime 

def hour():
    actual_hour= datetime.now()
    return actual_hour
    
print(hour())
