'''numerology.py - numerological functions'''

MASTER_NUMBERS = ("11", "22", "33")

def _get_alphanum_values():
	alphanum_dict = {}

	for i in range(1, 27):
		letter = chr(i + ord('a') - 1)	
		value = i % 9
		if value == 0:
			value = 9
		alphanum_dict[letter] = str(value)
	
	for i in range(0, 10):
		i = str(i)
		alphanum_dict[i] = i
	
	return alphanum_dict

ALPHANUM_VALUES = _get_alphanum_values()


def final_sum(*numbers):
	'''returns the final numerological sum of given numbers'''
	x = 0
	for n in numbers:
		x += int(n)
	while x > 9:
		digits = map(int, str(x))
		x = sum(digits)
	return str(x)


def all_sums(*numbers):
	'''returns a tuple of the raw sum, secondary sum, and final sum
	of given numbers'''
	x = 0
	for n in numbers:
		x += int(n)
	raw_sum = x

	x0 = x
	while x > 9:
		x0 = x
		digits = map(int, str(x))
		x = sum(digits)
		
	return (str(raw_sum), str(x0), str(x))


def sum_word(word):
	'''returns the numerological value of a word as a tuple of the raw sum,
	secondary sum, and final sum'''
	x = 0
	for letter in word.lower():
		x += int(ALPHANUM_VALUES[letter])
	return all_sums(x)
