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
		self.run_main_menu()
	
	def run_main_menu(self):
		pass

	def run_analysis(self):
		pass

	def show_analysis_output(self, analysis):
		pass

	def plot_number_frequency(self, numbers):
		'''Display a pie chart of the frequencies each number occurs in list 
		`numbers`.'''
		labels = [str(i+1) for i in range(13)]
		freqs = [0] * 13
		for n in numbers:
			freqs[int(n)] += 1
			
		colors = [self.data.get_data(str(n), "hex") for n in range(1, 13)]

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


def run_analysis(text):
	data = Data(DATABASE)

	words = parsing.parse_words(text)
	word_sums = dict((w, numerology.sum_word(w)) for w in words)
	word_final_sums = [s[2] for s in word_sums.values()]
	total_sum = numerology.all_sums(*word_final_sums)

	number_info = dict()
	for number in set(word_final_sums):
		number_info[number] = data[number]

	for word, sums in word_sums.items():
		num_data = data[sums[2]]
		show_word_analysis(word, num_data)
	
	# mix colors and show output
	# print total sum


def run_from_file(filename):
	with open(filename) as fh:
		text = fh.read()
		run_analysis(text)


def run_from_prompt():
	pass


if __name__ == '__main__':
	pirouette = Pirouette(DATABASE)
	#pirouette.run()

	pirouette.plot_number_frequency([1,1,1,1,2,2,3,3,3,3,3,3,3,3,4,5,5,5,5,6,6,6,7,7,7,7,7,8,8,8,9,9,10, 10, 10,10,10,10,10,10,10,11,11,12])
