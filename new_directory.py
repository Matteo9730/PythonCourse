#write a program that creates a new directory

import os


def new(x):
    new_directory = x
    os.chdir("<path>")
    return os.mkdir(new_directory)


print(new("<directory>"))
