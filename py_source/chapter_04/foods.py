my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 

my_foods.append('cannoli') 
friend_foods.append('ice cream') 

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

friend1_foods = my_foods
friend1_foods.append("first")
my_foods.append("second")

print(friend1_foods)
print(my_foods)
