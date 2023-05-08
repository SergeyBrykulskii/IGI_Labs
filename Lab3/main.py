from parsers.json.json_parser import JsonParser
import os

file_path = './test.json'

x = {"a" : 12, "b" : 12,"c" : 13}

class A:
    def __init__(self) -> None:
        self.b = 3
        self.a = 3
    


def sm(a, b):
    return a + b

os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, 'w') as output_file:
    JsonParser.dump(sm, output_file)