from my_parser import ( count_average_sentence_length,
                        count_non_declarative_sentences,
                        count_average_word_length, 
                        count_number_of_letters,
                        count_sentences,
                        get_top_K_repeated_N_grams) 

def test_count_sentences_1():
    text = ''
    assert count_sentences(text) == 0


def test_count_sentences_2():
    text = 'AAAAAAA'
    assert count_sentences(text) == 0


def test_count_sentences_3():
    text = 'qwerty! Mr. Qwerty. No... Ms. Qwerty!!!'
    assert count_sentences(text) == 4


def test_count_sentences_4():
    text = 'QWERTY, qwerty!? qw.. Ph.D. qwERTY?'
    assert count_sentences(text) == 3


def test_count_sentences_5():
    text = '"qewr". qwe... 4 a.m. now!'
    assert count_sentences(text) == 3
    

def test_count_non_declarative_sentences_1():
    text = ''
    assert count_non_declarative_sentences(text) == 0


def test_count_non_declarative_sentences_2():
    text = 'AAAAAAA'
    assert count_non_declarative_sentences(text) == 0


def test_count_non_declarative_sentences_3():
    text = 'qwerty! Mr. Qwerty. No... Ms. Qwerty!!!'
    assert count_non_declarative_sentences(text) == 2


def test_count_non_declarative_sentences_4():
    text = 'QWERTY, qwerty!? qw.. Ph.D. qwERTY?'
    assert count_non_declarative_sentences(text) == 2


def test_count_non_declarative_sentences_5():
    text = '"qewr". qwe... 4 a.m. now!'
    assert count_non_declarative_sentences(text) == 1


def test_count_number_of_letters_1():
    text = ''
    assert count_number_of_letters(text) == 0


def test_count_number_of_letters_2():
    text = 'AAAAAAA'
    assert count_number_of_letters(text) == 7


def test_count_number_of_letters_3():
    text = 'qwerty! Mr. Qwerty. No... Ms. Qwerty!!!'
    assert count_number_of_letters(text) == 24


def test_count_number_of_letters_4():
    text = 'QWERTY, qwerty!? qw.. Ph.D. qwERTY?'
    assert count_number_of_letters(text) == 23


def test_count_number_of_letters_5():
    text = '"qewr". qwe... 4 a.m. now!'
    assert count_number_of_letters(text) == 12


def test_count_average_sentence_length_1():
    text = ''
    assert count_average_sentence_length(text) == 0


def test_count_average_sentence_length_2():
    text = 'AAAAAAA'
    assert count_average_sentence_length(text) == 0


def test_count_average_sentence_length_3():
    text = 'qwerty! Mr. Qwerty.'
    assert count_average_sentence_length(text) == 7


def test_count_average_sentence_length_4():
    text = 'qw.. Ph.D. qwERTY?'
    assert count_average_sentence_length(text) == 5.5


def test_count_average_sentence_length_5():
    text = 'qwe... 4 a.m. now!'
    assert count_average_sentence_length(text) == 4
    

def test_count_average_word_length_1():
    text = ''
    assert count_average_word_length(text) == 0


def test_count_average_word_length_2():
    text = 'AAAAAAA'
    assert count_average_word_length(text) == 7


def test_count_average_word_length_3():
    text = 'qwerty! Mr. Qwerty. No... Ms. Qwerty!!!'
    assert count_average_word_length(text) == 4


def test_count_average_word_length_4():
    text = 'QWERTY, qwerty!? qw.. Ph.D. qwTY?'
    assert count_average_word_length(text) == 3.5


def test_count_average_word_length_5():
    text = '"qewr". qwe... 4 a.m. now!'
    assert count_average_word_length(text) == 2.4


# def test_get_top_K_repeated_N_grams_1():
#     text = ''
#     assert get_top_K_repeated_N_grams(text) == 0


# def test_get_top_K_repeated_N_grams_2():
#     text = 'AAAAAAA'
#     assert get_top_K_repeated_N_grams(text) == 7


# def test_get_top_K_repeated_N_grams_3():
#     text = 'qwerty! Mr. Qwerty. No... Ms. Qwerty!!!'
#     assert get_top_K_repeated_N_grams(text) == 24


# def test_get_top_K_repeated_N_grams_4():
#     text = 'QWERTY, qwerty!? qw.. Ph.D. qwERTY?'
#     assert get_top_K_repeated_N_grams(text) == 23


# def test_get_top_K_repeated_N_grams_5():
#     text = '"qewr". qwe... 4 a.m. now!'
#     assert get_top_K_repeated_N_grams(text) == 12