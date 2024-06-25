#write a program that calculates the difference between two dates

from datetime import datetime
def res(x,y):
    if x>y: 
        x,y= y,x
    different= y-x
    return different.days

date1= datetime(2022, 2, 2)
date2= datetime(2023, 1, 10)
print(res(date1,date2))