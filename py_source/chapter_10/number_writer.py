import json

numbers = ['lian', 3, 5, 7, 11, 13]

filename = 'py_source\chapter_10\\numbers1.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
