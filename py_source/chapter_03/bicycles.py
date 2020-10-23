bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)
print(bicycles[2].upper())
print(bicycles)
bicycles[0]='LianJun'
print(bicycles)
bicycles.insert(2,"abc")
print(bicycles)
bicycles.__delitem__(2)
print(bicycles)
del bicycles[1]
print(bicycles)
