import re
from constants import *

def count_sentences(text: str) -> int:
    text = text.lower()
    amount_of_sentences = len(re.findall(SENTENCE_REGEX, text))

    for abbreviation in ONE_WORD_ABBREVIATION:
        amount_of_sentences -= text.count(abbreviation)

    for abbreviation in TWO_WORD_ABBREVIATION:
        amount_of_sentences -= text.count(abbreviation)
    return amount_of_sentences
    
def count_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECLARATIVE_SENTENCE_REGEX, text))

