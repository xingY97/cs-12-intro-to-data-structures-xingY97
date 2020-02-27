import sys

word_histogram = {}
def histogram(lines):
    
    for word in lines:
        words = word.split()
        #print(words)
        for w in words:
            #get method searches for specific key, else it will return 0 as default value
            word_histogram[w] = word_histogram.get(w,0) + 1
    return word_histogram

def unique_words(histogram):
    
    word_txt = open(filename,'r')
    count = {}
    for word in word_txt:
        if word in count :
            count[word] += 1
        else:
            count[word] = 1
    len(count) 
    print(f"number of unique words are {len(count)} ")


# def frequency(word，histogram):
#     frequencies = []
#     return histogram[word]

def get_index(word,listogram):
    current_index = 0
    for item in listogram:
        if item[0] == word:
            return current_index
        else:
            current_index += 1
    return -1


def listogram(lines):
    listogram = []
    for word in lines:
        word = word.rstrip()
        index = get_index(word,listogram)
        if index == -1: #first time we are seeing this 
            listogram.append([word,1])
        else: #need to update count
            listogram[index][1] += 1
    return listogram


def tuplegram(lines):
    tuplegram = []
    for word in lines:
        word = word.rstrip()
        index = get_index(word,tuplegram)
        if index == -1: #first time we are seeing this word
            tuplegram.append((word,1))
        else:#need to update count
            newcount = tuplegram[index][1] + 1
            tuplegram[index] = (word,newcount)
    return tuplegram



if __name__ == "__main__":

    filename = "words.txt"
    lines = open(filename,'r')

    histogram(lines)

    unique_words(histogram)







        
    



