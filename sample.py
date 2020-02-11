
from random import randint
from histogram import histogram

def weighted_sample(histogram):

    tokens = sum(count for word, count in histogram.items()) #count total tokens
    dart = randint(1,tokens)

    fence = 0 #border of where each word splits the number line
    for word, count in histogram.items():
        fence += count # Move this word's fencce birder to the right
        if fence >= dart: #Check if this word's fence is past the dart
            return word # fence is past the dart, so choose this word 
    

if __name__ == "__main__":
    filename = "words.txt"
    lines = open(filename,'r').read().splitlines()
    h = histogram(lines)
    #print(h)
    print(weighted_sample(h))
    