import sys as sys
import random 

arguments = sys.argv[1:]

def rearrange():
    for word in arguments:
        word = random.randint(0,len(arguments) - 1)
        print(arguments[word])

rearrange()


        





