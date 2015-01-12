import re

def parse_words(text):
	# Remove apostrophes
	text = re.sub("['\[\]]", "", text)

	delimiter = "[a-zA-z0-9]*"
	return re.findall(delimiter, text)


