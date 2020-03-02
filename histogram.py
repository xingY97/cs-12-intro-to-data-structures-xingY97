from __future__ import division, print_function
from random import randint, choice, seed
seed(1) 
import re 

class Histogram(dict): 
    def __init__(self, lines=None): 
        """Initialize this histogram as a new list and count given words."""
        filename = "words.txt"
        my_histogram = open(filename,'r')
        super(Histogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.unique_words_count = 0  #count of unique word 
        self.words_count = 0  #total count of all words #tokens
        self.words = [] 
        if lines != None: 
            for line in lines:
                words_from_line = re.sub("[^\w]", " ",  line).split() #turns every word in line to a list of words
                for word in words_from_line: 
                    self.count(word)
    
    def count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        if self.frequency(word) > 0:
            self[word] += count # check if the word appears alread if yes add 1 to count.
        else: 
            self[word] = count
            self.unique_words_count += 1 # if an unique word appears, add 1 to unique word count 
        self.words_count += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if not self.__contains__(word):
            return 0
        frequency = self[word]
        return frequency

    def get_count(self, word):
        word_count = 0
        for word in self:
            word_count = self.get(word, 0) + 1  #get method searches for specific key, else it will return 0 as default value, else adds 1
            self[word] = word_count

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        for word_history in self:
            if word == word_history:
                return True
        return False

def create_histogram(source_text):
    '''create a Histogram from a string'''
    return Histogram(source_text)

def get_unique_words(histogram):
    '''get total count of unique words in the histogram'''
    return histogram.unique_words

def get_frequency(word, histogram):
    ''' get the frequency of a word from the histogram'''
    return histogram.frequency(word)

def word_contains(word, histogram):
    if histogram.__contains__(word):
        return True
    return False

if __name__ == '__main__':
    
    filename = "words.txt"
    my_histogram = open(filename,'r')
    #my_histogram = Histogram("one fish two fish red fish ") #initialize a histogram from a string
    print(f"Histogram = {my_histogram}")
    print(f"Unique words count = {my_histogram.unique_words_count}")
    print(f"Words count = {my_histogram.words_count}")
    word = "fish"
    does_contain = f"appears {my_histogram.frequency(word)}x in" if word_contains(word, my_histogram) else "does not appear in"
    print(f"{word} {does_contain} the following histogram: {my_histogram}")