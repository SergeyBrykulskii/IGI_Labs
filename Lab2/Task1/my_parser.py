import re
from collections import Counter
from constants import (SENTENCE_REGEX, ONE_WORD_ABBREVIATION, TWO_WORD_ABBREVIATION,
                       NON_DECLARATIVE_SENTENCE_REGEX, WORD_REGEX)


def count_sentences(text: str) -> int:
    text = text.lower()
    number_of_sentences = len(re.findall(SENTENCE_REGEX, text))

    for abbreviation in ONE_WORD_ABBREVIATION:
        number_of_sentences -= text.count(abbreviation)

    for abbreviation in TWO_WORD_ABBREVIATION:
        number_of_sentences -= text.count(abbreviation) * 2
    return number_of_sentences
    

def count_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECLARATIVE_SENTENCE_REGEX, text))


def count_number_of_letters(text: str) -> int:
    words = re.findall(WORD_REGEX, text)

    number_of_letters = 0
    for word in words:
        number_of_letters += len(word)
    return number_of_letters


def count_average_sentence_length(text: str) -> float:
    number_of_sentences = count_sentences(text)
    number_of_letters = count_number_of_letters(text)

    if number_of_sentences == 0:
        return 0
    
    return number_of_letters / number_of_sentences


def count_average_word_length(text: str) -> float:
    words = re.findall(WORD_REGEX, text)
    number_of_letters = count_number_of_letters(text)
    if len(words) == 0:
        return 0
    return number_of_letters / len(words)


def get_top_K_repeated_N_grams(text: str, k=10, n=4) -> list:
    words = re.findall(WORD_REGEX, text)
    
    n_grams = []
    n_grams.extend(list(zip(*[words[i:] for i in range(n)])))
    counter = dict() 

    for n_gram in n_grams:
        key = ' '.join(n_gram)
        counter.setdefault(key, 0)
        counter[key] += 1

    k_most_common_n_grams = dict(list({key: value for key, value in sorted(
        counter.items(), key=lambda item: item[1], reverse=True)}.items())[:k])

    return k_most_common_n_grams
