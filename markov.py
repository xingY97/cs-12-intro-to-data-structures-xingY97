from dictogram import Dictogram

class MarkovChain:

    def __init__(self, word_list):


        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(word_list)
         self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                histogram[next_word] = histogram.get(next_word, 0) + 1
            else: #first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        #TODO: generate a sentence num_words long using the markov chain
        sentence = ""
        first_word = "fish" #fish for testing
        
        print("FIRST WORD IS", first_word)
        sentence += first_word + " "
        index = 0
        while index < num_words: 
            current_word = first_word
            for word, histogram in self.markov_chain.items(): 
                if current_word == word: #look for our current word in our markov chain
                    current_word_dictogram = histogram
                    print("From word =", word, "DICTOGRAm I AM SAMPLING IS", current_word_dictogram)
                    random_weighted_word = histogram.sample() #get the random_weighted_word
                    print("Sample returned is", random_weighted_word)
                    current_word = random_weighted_word #assign random_word as the current_word
                    if index == num_words - 1: #if this is the last word, add "."
                        sentence += current_word + "."
                    else: #if not last word, add a space in the end
                        sentence += current_word + " "
                    break
                else:
                    continue
            index += 1
        print("SENTENCE =", sentence)
        return sentence
        

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))