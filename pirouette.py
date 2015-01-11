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

	'''
	text = "Sense and Sensibility is a 1995 period drama film directed by Ang Lee and based on Jane Austen's 1811 novel of the same name. Actress Emma Thompson (pictured) wrote the script and stars as Elinor Dashwood, while Kate Winslet plays Elinor's younger sister Marianne; actors Hugh Grant and Alan Rickman appear as their respective suitors. The story follows two English sisters from a wealthy family (wealthier in the film than the book) who become destitute and seek financial security through marriage. The film was released in December 1995 in the US and two months later in Britain. A commercial success, it garnered overwhelmingly positive reviews upon release and received many accolades, including three awards and eleven nominations at the 1995 British Academy Film Awards. It earned seven Academy Awards nominations, including for Best Picture and Best Actress (for Thompson). The actress won for Best Adapted Screenplay, becoming the only person to have received Academy Awards for both acting and screenwriting. Sense and Sensibility contributed to a resurgence in popularity for Austen's works, and has led to many more productions in similar genres. It persists in being recognised as one of the best Austen adaptations of all time"
	delimiter = "[a-zA-z0-9]*"
	result = parse(text, delimiter)
	pprint(result)

	lnd = get_letter_numerology_dict()
	result = sum_word("EdwardLeeNeal", lnd)
	pprint(result)
	'''
