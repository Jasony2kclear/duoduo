import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n\nnew one !\n")
from pizza import make_pizza
make_pizza(18,'abc')

from pizza import * 
make_pizza(18,'cef')