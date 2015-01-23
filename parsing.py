import re

from pyphen import Pyphen

def parse_words(text):
    '''returns a list of words given a string of alphanumeric words
    separated by spaces and punctuation'''
    # Remove apostrophes
    text = re.sub("['\[\]]", "", text)

    word = "\w+"
    return re.findall(word, text)


def parse_paragraphs(text):
    paragraph = ".+"
    return re.findall(paragraph, text)


def parse_sentences(text):
    sentence = "[^.?!]+[.?!]"
    return re.findall(sentence, text)


def count_syllables(word):
    '''returns the number of syllables in a word'''
    dic = Pyphen(lang="en_US")
    hyphenated = dic.inserted(word)
    return hyphenated.count('-') + 1
