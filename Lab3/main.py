from parsers.json.json_parser import JsonParser
from parsers.xml.xml_parser import XmlParser
import os

file_path_xml = './test.xml'
file_path_json = './test.json'

x = 5
    
y = [1]

def sm(a, b):
    return a + b

# s = "<tuple></tuple>"

# print(s[:-1])

class Person:
    religion = "aboba"

    def __init__(self, age=3):
        self.age = age

    def get_age(self):
        return self.age

os.makedirs(os.path.dirname(file_path_json), exist_ok=True)
with open(file_path_json, 'w') as output_file:
    JsonParser.dump(Person, output_file)

with open(file_path_json, 'r') as input_file:
    a = JsonParser.load(input_file)
    per = Person()
    p = a()
    print(p.get_age() == per.get_age())
os.makedirs(os.path.dirname(file_path_xml), exist_ok=True)
with open(file_path_xml, 'w') as output_file:
    XmlParser.dump(sm, output_file)

with open(file_path_xml, 'r') as input_file:
    a = XmlParser.load(input_file)
    print(sm(2, 4))
