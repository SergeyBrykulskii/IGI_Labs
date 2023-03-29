from core import (get_source, get_text_from_file,
                  get_text_from_console, input_results)
from constants import DEFAULT_TEXT

def main():

    source = get_source()

    match source:
        case 'f':
            text = get_text_from_file()
        case 'c':
            text = get_text_from_console()
        case 'd':
            text = DEFAULT_TEXT

    n = 4
    k = 10
    ans = input('Do you want change default n ans k(y/n):   ')
    if ans == 'y':
        while True:
            n = input('Enter n:   ')
            k = input('Enter k:   ')
            if n.isdecimal() and k.isdecimal():
                return
            else:
                print('Try again')

    input_results(text, n, k) 

if __name__ == "__main__":
    main()