import json
from os import sys

filename = sys.path[0] + '/numbers1.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
    
print(numbers)
