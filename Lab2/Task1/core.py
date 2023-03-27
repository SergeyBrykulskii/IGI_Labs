from my_parser import (count_sentences, count_non_declarative_sentences,
                       count_average_sentence_length, count_average_word_length,
                       get_top_K_repeated_N_grams)
from constants import (INVALID_TEXT_REGEX, SOURCE_VARIANTS) 
import re


def get_source() -> str:
    while True:
        choice = input('Choose source of the text file(f)/console(c)/default(d): ')
        if (choice in SOURCE_VARIANTS):
            if len(choice) > 1:
                return choice[0]
            return choice
        else:
            print('Try again')


def get_text_from_console() -> str:
    while True:
        text = input('Enter text(text must contain only letters, numbers and separators): ')

        if re.findall(INVALID_TEXT_REGEX, text):
            print("Try again")
        else:
            return text
        

def get_text_from_file(path='input.txt') -> str:
    f = open(path)
    text = f.read()
    text.replace('\n', ' ')
    text.replace('\t', ' ')
    if re.findall(INVALID_TEXT_REGEX, text):
        print("Invalid text")
        text = ""
    return text


def input_results(text: str):
    print('Amount of sentences in the text: ', count_sentences(text))
    print('Amount of non-declarative sentences in the text: ', count_non_declarative_sentences(text))
    print('Average length of the sentence in characters: ', count_average_sentence_length(text))
    print('Average length of the word in the text: ', count_average_word_length(text))
    print('Top-K repeated N-grams in the text: ', get_top_K_repeated_N_grams(text))