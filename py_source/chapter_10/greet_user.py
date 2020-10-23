import json
from os import sys
filename = sys.path[0] + '/username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
