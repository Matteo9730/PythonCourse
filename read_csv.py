"""
write a program that uses the csv library to read data from a csv file containing numbers and then calculate some
statistics, such as the average and the sum of the numbers
"""

import csv

def read(x):
    data = []
    with open(x, 'r') as file:
        player_csv = csv.reader(file)
        for rows in player_csv:
            for element in rows:
                y= [float(element)]
                data.extend(y)
    return data

def average(x):
    if not x:
        return 0
    return sum(x) / len(x)

def sum(y):
    return sum(y)

name_file = '<name.file>' #Enter a file here
data = read(name_file)
res1 = average(data)
res2 = sum(data)
print("I numeri sono: ", data)
print("La media è ", res1)
print("La somma è ", res2)