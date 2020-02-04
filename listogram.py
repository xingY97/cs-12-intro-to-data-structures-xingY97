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
        word 
