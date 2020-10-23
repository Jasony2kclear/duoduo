import json
from os import sys

numbers = [2, 3, 5, 7, 11, 13]

filename = sys.path[0] + '/numbers1.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
