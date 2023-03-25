ONE_WORD_ABBREVIATION = [
    'mon.', 'tue.', 'wed.', 'thu.', 'fri.', 'sat.', 'sun.', 
    'yr.', 'jan.', 'feb.', 'mar.', 'apr.', 'jun.', 'jul.', 
    'aug.', 'sep.', 'oct.', 'nov.', 'dec.', 'pl.', 'ex.', 
    'edu.', 'rf.', 're.', 'par.', 'pp.', 'p.', 'prep.', 
    'adv.', 'adj.', 'v.', 'n.', 'sr.', 'jr.', 'etc.', 'mr.',
    'ms.', 'mrs', 'smb.', 'smth.']
TWO_WORD_ABBREVIATION = ['e.g.', 'i.e.', 'p.m.', 'a.m.', 'p.s.', 'ph.d.']

SENTENCE_REGEX = r'[.!?]+'
NON_DECLARATIVE_SENTENCE_REGEX = r'[!?]+'
WORD_REGEX = r'\w*[a-zA-Z]\w*'
NUMBER_REGEX = r'^\d\w+| \d\w+'
INVALID_TEXT_REGEX =r'[^\w^ ^,^.^!^?]'
SOURCE_VARIANTS = ['file', 'console', 'default', 'f', 'c', 'd']
DEFAULT_TEXT = 'qwerty!'