# This program says hello and ask for my name.

print('Hello world!')
print('What is your name?') # as for their name
Name = input()
print('It is good to meet you, ' + Name)
print('The length of your name is:')
print(len(Name))
print('What is your age?') # ask for their age
age = input()
print('You will be ' + str(int(age) + 1) + ' in a year.')
if Name == 'Alice':
    print('Hi, Alice.')
elif int(age) < 12:
    print('You are not Alice, kiddo.')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif int(age)>100:
    print('You are not Alice, grannie.')
else:
    print('You are not Alice, friend.')
    
