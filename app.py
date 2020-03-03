from flask import Flask
from histogram import Histogram
from sample import weighted_sample
from markov import MarkovChain

app = Flask(__name__)


@app.route('/')
def generate_words():
    #build a histogram
    my_file = open("words.txt","r")
    lines = my_file.readlines()
    my_histogram = Histogram(lines)
    word_list = []
    for line in lines:
        for word in line.split():
            word_list.append(word)

    word = weighted_sample(my_histogram)
    #return word

    sentence = ""
    num_words = 7
    # for i in range(num_words):
    #     word = weighted_sample(my_histogram)
    #     sentence += " " + word
    markovChain = MarkovChain(word_list)
    sentence = markovChain.walk(num_words)
    print("sentence", sentence)
    return sentence

if __name__ == '__main__':
    
    app.run()