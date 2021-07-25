filename = 'py_source\ichapter_10\pi_digits.txt'
all_line=''
str3=''
try:
    with open(filename) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    print('sorry file not found')
    exit()
for line in lines:
    print(line.rstrip())
    all_line = all_line+ line.strip()
#str3=all_line.replace(' ','')
print(all_line)