import os
import json
import re

class Storage:
    def __init__(self, current_username):
        self._current_username = current_username
        self._file_path = "./user_data/" + current_username + ".json"
        self._data = set()
        self.load()


    def load(self):
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as input_file:
                self._data = set(json.load(input_file))


    def add(self, key: str):
        self._data.add(key)


    def remove(self, key: str):
        if key in self._data:
            self._data.remove(key)


    def save(self):
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        with open(self._file_path, 'w') as output_file:
            json.dump(list(self._data), output_file)

    
    def list(self) -> set:
        return self._data
    

    def grep(self, regex: str):
        valid_elements = list(filter(lambda x: re.match(regex, x), self._data))
        return valid_elements
        
    
    def find(self, key: str) -> bool:
        return key in self._data


    def switch(self, new_username):
        self._current_username = new_username
        self._file_path = "./user_data/" + new_username + ".json"
        self._data.clear()
        self.load()

