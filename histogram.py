def histogram():
    '''
    takes a cource_text argument and return a histogram data
    structure that stores each unique words along with the numbe of times 
    the word appears in the source text'''
    
    filename = "words.txt"
    lines = open(filename,'r')

    word_histogram = {}

    for word in lines:
        words = word.split()
        print(words)
        for w in words:
            word_histogram[w] = word_histogram.get(w,0) + 1
    print(word_histogram)
    
histogram()


def unique_words():
    '''function that takes a histogram argument and retuns the total count of 
    unique words in the histogram'''

def frequency():
    '''takes a word and histogram argument and retuns the number of times that
     word appears in a text.'''



