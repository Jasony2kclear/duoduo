import os
print(os.getcwd())
real_path = os.sys.path[0]
filename = real_path + "/pi_digits.txt"
print(filename)

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

for line in lines:
    print(line.rstrip())