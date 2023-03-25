from core import *

source = get_source()

match source:
    case 'f':
        text = get_text_from_file()
    case 'c':
        text = get_text_from_console()
    case 'd':
        text = DEFAULT_TEXT


input_results(text)