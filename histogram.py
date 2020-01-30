import sys
from collections import Counter


def histogram():
    '''
    takes a cource_text argument and return a histogram data
    structure that stores each unique words along with the numbe of times 
    the word appears in the source text'''
    word_histogram = {}
    for word in lines:
        words = word.split()
        #print(words)
        for w in words:
            word_histogram[w] = word_histogram.get(w,0) + 1
    print(word_histogram)


def unique_words(lines):
    '''function that takes a histogram argument and retuns the total count of 
    unique words in the histogram'''

    uniqueWordCount = 0
    word_txt = open(filename,'r')
    count = {}
    for word in word_txt:
        if word in count :
            count[word] += 1
        else:
            count[word] = 1
    len(count) 
    print(len(count))
    

    

def frequency():
    '''takes a word and histogram argument and retuns the number of times that
     word appears in a text.'''



if __name__ == "__main__":
    filename = "words.txt"
    lines = open(filename,'r')
    histogram()
    unique_words(lines)


