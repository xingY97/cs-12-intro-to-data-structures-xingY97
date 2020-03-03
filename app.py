from flask import Flask
from histogram import histogram
from sample import weighted_sample
from markov import MarkovChain

app = Flask(__name__)


@app.route('/')
def generate_words():
    #build a histogram
    my_file = open("words.txt","r")
    lines = my_file.readlines()
    my_histogram = histogram(lines)
    word_list = []
    for line in lines:
        for word in line.split():
            word_list.append(word)

    word = weighted_sample(my_histogram)
    #return word

    sentence = ""
    num_words = 5
    # for i in range(num_words):
    #     word = weighted_sample(my_histogram)
    #     sentence += " " + word
    MarkovChain = MarkovChain(word_list)
    sentence = MarkovChain.walk(num_words)
    return sentence

if __name__ == '__main__':
    
    app.run()