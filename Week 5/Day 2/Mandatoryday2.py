# Exc 1
class Pet():
    animals = []
    def __init__(self, animals):
        self.animals = animals
       

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Persian(Cat):
    pass


my_cats=[ ]
my_cats.append(Chartreux('Terry',5))
my_cats.append(Bengal('Jim',7))
my_cats.append(Persian('Tim',12))
my_pet=Pet(my_cats)
my_pet.walk()

# Exc 2
class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        
    def bark(self):
        print('bark bark bark')

    def run_speed(self):
        speed =(self.age/self.weight)*10
        print(speed)
        return speed
        

    def fight(self ,other_dog,):
        
        if self.run_speed() > other_dog.run_speed():
            print('This dog wins')
        else:
            print("Other dog wins")   
     
dog1=Dog('Doggy1',12,32)
dog2=Dog('Doggy2',10,30)
dog3=Dog('Doggy3',9,31)
dog3.bark()
dog3.fight(dog2)
dog1.run_speed()

