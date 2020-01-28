import sys as sys
from random import randint
import random

arguments = int(sys.argv[1])

filename = "/usr/share/dict/words"


my_file = open(filename, "r")

lines = my_file.readlines()



def rearrange():
    for word in range(arguments):
        word = random.randint(1, len(lines) - 1)
        print(lines[word])

rearrange()
