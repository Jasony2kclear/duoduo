class Dog():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def sit(self):
        print("Let's sit :"+self.name.title())
    def howold(self):
        print(str(self.age)+' is your old this year!\n')

Jason=Dog('jason', 8)
Lian=Dog('LianJun', 50)

Jason.sit()
Jason.howold()