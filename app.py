from flask import Flask
from histogram import histogram
#from sample import weighted_sample

app = Flask(__name__)


@app.route('/')
def generate_words():
    #build a histogram
    my_file = open("./words.txt","r")
    lines = my_file.readlines()
    my_histogram = histogram(lines)

    #word = weighted_sample(my_histogram)
    return "test string"

if __name__ == '__main__':
    app.run()