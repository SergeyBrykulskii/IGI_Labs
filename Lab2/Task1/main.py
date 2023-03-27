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


    input_results(text) 

if __name__ == "__main__":
    main()