motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

popup_moto = motorcycles.pop()
print(popup_moto)
print(motorcycles)
popup_moto0 = motorcycles.pop(0)
print(motorcycles)