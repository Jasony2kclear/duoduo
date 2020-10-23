alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original position: " + str(alien_0['x_position']))
alien_1 = {'x1':'This is first item','x2':'This is second item'}
if alien_1['x2']=='This is first item':
    print("Let find the word: " + str(alien_1['x2']))
else:
    print("other")

alien_1['x3']=100
print(alien_1['x3'])
print(alien_1)
alien_1['x3']=200
print(alien_1['x3'])
del alien_1['x3']
print(alien_1)

# Move the alien to the right.
# Figure out how far to move the alien based on its speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New position: " + str(alien_0['x_position']))
