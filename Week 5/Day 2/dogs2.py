from Mandatoryday2 import Dog
import random
 
class PetDog(Dog):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)
        self.trained=False

    def train(self):
        print('bark')
        self.trained= True

    def play(self,*dogs_names ):
        names =" ".join( list(dogs_names))
        print (f" The  dogs: {names} play together ")
        for dog in dogs_names:
           if self.trained:
                self.trained=False


    def do_a_trick(self):
        value=random.randint(0,3)
        if not self.trained:
            if value==0:
                print(f'{self.name} does a barrel roll')
            elif value==1:
                print(f'{self.name} stands on their back legs')  
            elif  value==2: 
                print(f'{self.name}shakes your hand') 
            elif value==3:
                print(f'{self.name} plays dead')       

pet1=PetDog("jimmy",12,13)  
pet1.do_a_trick()
pet1.play("jim",'dan')
 
#  Exc 4
class Family:
    def __init__(self,members,last_name):
        self.members=members
        self.last_name=last_name

    def born(self,**new_member):
        self.members.append(new_member)
        print(f'Lets welcome {self.members[-1]["name"] } to the family!')

    def is_18(self,name):
        for member in self.members: 
            if name != member['name']:
                continue         
            elif member['age'] >18 :
                print('yes')
                return True
            else:
                print('no')    
    def nice_presentation(self,last_name):
        if last_name != self.last_name:
            print('This family does not exist')
        else:
            print(f"Thes are the members of family {last_name}")
            for member in self.members:
                print(f"{member['name']}:{member['age']}")
    


family1=Family([ {'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False}],'Hobbs' )
family1.born(name='Mitch',age=0,gender='Male',is_child=False)
family1.is_18("Mitch")
family1.nice_presentation('Hobbs')

# Exc 5
class Incredibles(Family):
    def __init__(self, members, last_name, power, incredible_name):
        super().__init__(members, last_name)
        self.power = power
        self.incredible_name = incredible_name
    def use_power(self):
        try:
            if self.members['age'] > 18:
                print(f"Your power is: {self.members['power']}")
        except:
            print(f"{self.members['name']} isn't over 18")
    def incredible_presentation(self):
        for item in self.members:
            print(item)
incredible_family = Incredibles([ {'name':'Bob','age':35,'gender':'Male','is_child':False}, {'name':'Helen','age':32,'gender':'Female','is_child':False}, {'name':'Violet','age':12,'gender':'Female','is_child':True}, {'name':'Dashiell','age':8,'gender':'Male','is_child':True}], "Parr", [{'power': 'super-strength'}, {'power': 'invisible'}, {'power': 'force-shield'}, {'power': 'super-speed'}], [{'incredible_name': 'Mr. Incredible'}, {'incredible_name': 'Elastigirl'}, {'incredible_name': 'Vi'}, {'incredible_name': 'Dash'}])

incredible_family.incredible_presentation()
incredible_family.born(name="Jack", age=3, gender="Male", is_child=True, incredible_name='Jack-Jack', power='Unknown power')
incredible_family.incredible_presentation()























