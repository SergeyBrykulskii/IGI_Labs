import re
from constants import *

def count_sentences(text: str) -> int:
    text = text.lower()
    number_of_sentences = len(re.findall(SENTENCE_REGEX, text))

    for abbreviation in ONE_WORD_ABBREVIATION:
        number_of_sentences -= text.count(abbreviation)

    for abbreviation in TWO_WORD_ABBREVIATION:
        number_of_sentences -= text.count(abbreviation)
    return number_of_sentences
    
def count_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECLARATIVE_SENTENCE_REGEX, text))

def count_average_sentence_length(text: str) -> float:
    number_of_sentences = count_sentences(text)

    number_of_words = len(re.findall(WORD_REGEX, text))
    amount_of_numbers = len(re.findall(NUMBER_REGEX, text))
    return (number_of_words - amount_of_numbers) / number_of_sentences

