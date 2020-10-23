prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
  
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
message1 = input("How old are you")
print(message1)
if message1 == '7':
    print("yes your old is",message1)

if int(message1) == 7:
    print("yes your old is(int)",message1)

while True:
    message = input(prompt)
    
    if message == 'quit':
       break 
    else:
        print(message)