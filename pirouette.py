from pprint import pprint
from sys import argv

import numerology
import parsing


def show_result(word_sums, total_sum):
	print("Here are the numerological values for each word:")
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



def run_parser(text):
	words = parsing.parse_words(text)
	word_sums = dict((w, numerology.sum_word(w)) for w in words)
	word_final_sums = [s[2] for s in word_sums.values()]
	total_sum = numerology.all_sums(*word_final_sums)

	show_result(word_sums, total_sum)


def run_from_file(filename):
	with open(filename) as fh:
		text = fh.read()
		run_parser(text)


def run_from_prompt():
	pass


if __name__ == '__main__':
	print('=' * 72)
	print("*** Welcome to Pirouette ***")
	print('=' * 72)
	print()

	if len(argv) > 1:
		run_from_file(argv[1])
	else:
		run_from_prompt()
