import json

filename = 'py_source\chapter_10\\numbers1.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
    
print(numbers)
