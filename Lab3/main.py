from parsers.json.json_parser import JsonParser
import os

file_path = './test.json'

x = [12, 12, 13]

class A:
    b = 3
    

os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, 'w') as output_file:
    JsonParser.dump(x, output_file)