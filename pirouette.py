from collections import OrderedDict
from sys import argv

import matplotlib.pyplot as plt

import color
from data import Data
import numerology
import parsing


DATABASE = "data.db"


class Pirouette:

    def __init__(self, database):
        self.data = Data()
        self.data.load(database)
    
    def run(self):
        #self.run_main_menu()
        with open(argv[1]) as fh:
            text = fh.read()
        self.run_analysis(text)
    
    def run_main_menu(self):
        pass

    def run_analysis(self, text):
        words = parsing.parse_words(text)
        word_sums = dict((w, numerology.sum_word(w)) for w in words)
        word_final_sums = [s[2] for s in word_sums.values()]
        total_sum = numerology.all_sums(*word_final_sums)

        #for word, sums in word_sums.items():
            #num_data = self.data[sums[2]]
            #show_word_analysis(word, num_data)

        self.plot_number_frequencies(word_final_sums)

    def show_analysis_output(self, analysis): pass

    def plot_number_frequencies(self, numbers):
        '''Display a pie chart of the frequencies each number occurs in
        list of integer strings `numbers`.'''
        ns = 12

        labels = []
        length = float(len(numbers))
        for i in range(1, ns+1):
            name = str(i)
            pct = numbers.count(name) / length
            label = "{0}\n{1:.2%}".format(name, pct)
            labels.append(label)

        freqs = [0] * ns 
        for n in numbers:
            freqs[int(n)-1] += 1
                
        colors = [self.data.get_data(str(n), "hex")
                    for n in range(1, ns)]

        plt.pie(freqs, labels=labels, colors=colors)
        plt.axis('equal')
        plt.show()


def show_word_analysis(word, sec_data, fin_data):
    print()
    for word, sums in word_sums.items():
        line = word + "\t\t" \
                + str(sums[0]) + ', ' \
                + str(sums[1]) + ', ' \
                + str(sums[2])
        print(line)
    print()

    print("Total value: " + str(total_sum))
    print("Word count: " + str(len(word_sums)))


if __name__ == '__main__':
    pirouette = Pirouette(DATABASE)
    pirouette.run()
