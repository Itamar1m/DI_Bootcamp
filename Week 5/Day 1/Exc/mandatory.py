# XP
# Exc1
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat1=Cat('kitty',12)
# cat2=Cat('tommy',7)
# cat3=Cat('garcie',2)

# cats=[cat1,cat2,cat3]

# def oldest_cat():
#     oldest=0
#     name= ''
#     for cat in cats:
#         if cat.age > oldest:
#             oldest=cat.age
#             name =cat.name
#     print(f'The oldest cat is {name} and is {oldest} years old ')
#     return (oldest,name)
    
# oldest_cat()

# # Exc 2
# class Dog:
#     def __init__(self,name,height):
#         self.name=name 
#         self.height=height

#     def bark(self):
#         print(f"{self.name} goes woof!") 

#     def jump(self):
#         print(f'and jumps {self.height*2} cm high.')

# davids_dog=Dog("Rex",50)
# davids_dog.bark()
# davids_dog.jump()

# saras_dog=Dog("Teacup",20)
# saras_dog.bark()
# saras_dog.jump()

# if saras_dog.height>davids_dog.height:
#     print(saras_dog.name)
# else:
#     print(davids_dog.name)    

# Exc 3
class Song:
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self ):
        for lyric in self.lyrics:
            print(lyric)    

stairway=Song(['There’s a lady whos sure','all that glitters is gold','and she’s buying a stairway to heaven'])
stairway.sing_me_a_song()

# Exc 4
class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animals=['lion','lemur' ,'tiger','monkey','giraffe']
        self.dictionary={}

    def add_animal(self,new_animal):
        if new_animal not in self.animals:

            self.animals.append(new_animal)
    
    def get_animals(self):
        print(" ".join(self.animals))
        
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        new_list=[]
        for animal in self.animals:
            if not new_list:
                new_list.append([animal])
            else:
                added=False
                for sub_list in new_list:
                    if sub_list[0][0]==animal[0]:
                        sub_list.append(animal)
                        added=True             
                if not added:                    
                        new_list.append([animal])     
        
        for index,sub_list in enumerate (new_list):
            self.dictionary.update({index+1:", ".join(sub_list)})
            
        print(self.dictionary)

    def get_groups(self):
        for item in self.dictionary.items():
            print({item})




ramat_gan_safari=Zoo('ramat_gan_safari')
ramat_gan_safari.get_animals()
print('Which animal should we add to the zoo --> ant')
ramat_gan_safari.add_animal('ant')
ramat_gan_safari.get_animals()
print('Which animal should sell from the zoo --> tiger')
ramat_gan_safari.sell_animal('tiger')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()



