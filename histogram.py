import sys
from collections import defaultdict

filename = "words.txt"
lines = open(filename,'r')

def histogram():
    word_histogram = {}
    for word in lines:
        words = word.split()
        #print(words)
        for w in words:
            word_histogram[w] = word_histogram.get(w,0) + 1
    print(word_histogram)


def unique_words(word_histogram):
    
    word_txt = open(filename,'r')
    count = {}
    for word in word_txt:
        if word in count :
            count[word] += 1
        else:
            count[word] = 1
    len(count) 
    print(f"number of unique words are {len(count)} ")

def frequency():
    pass


if __name__ == "__main__":

    histogram()
    unique_words(lines)



