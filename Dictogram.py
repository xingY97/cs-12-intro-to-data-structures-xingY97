class Dictogram:

    def__init__(self)
    #dictionary type histogram init
    self.histogram = {}

    def build_histogram(self,lines):
    for word in lines:
        words = word.split()
        #print(words)
        for w in words:
            #get method searches for specific key, else it will return 0 as default value
            word_histogram[w] = word_histogram.get(w,0) + 1
   
   def get_frequency(self, word):
       return self.histogram[word]

    