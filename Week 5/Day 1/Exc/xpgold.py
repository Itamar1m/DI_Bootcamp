# # Exc 1
# class Circle:
#     def __init__(self,radius=1.0):
#         self.radius=radius
       
#     def calc_area(self):
#         r=float(self.radius)
#         area=3.14*r*r
#         print(f"Area of Circle: {area}")
#         return area

#     def calc_perimeter(self):
#         r=float(self.radius)
#         perimeter=2*3.14*r                        
#         print(f"Perimeter of Circle:  {perimeter}")
#         return perimeter

# circle=Circle(3)
# circle.calc_perimeter()
# circle.calc_area()

# # Exc 2
# class MyList:
#     def __init__(self,non_empty_list):
#         self.non_empty_list=non_empty_list

#     def check_if_list(self):
#         if type(self.non_empty_list) != list or len(self.non_empty_list) <1:
#             return True

#     def reverse_list(self):
#         if self.check_if_list():
#             print("You list input is invalid") 
#         else:
#             self.non_empty_list.reverse()
#             print(self.non_empty_list)

#     def sort_list(self):
#         if self.check_if_list():
#                 print("You list input is invalid") 
#         else:
#             self.non_empty_list.sort()
#             print(self.non_empty_list)

   
#     def random_num_list(self):
#         import random
#         random_numbers=[ random.randrange(1,100)for i in range(len(self.non_empty_list))]
#         print(random_numbers)
    

# new_list=MyList(["a","b","e","c","d"])
# new_list.reverse_list()
# new_list.sort_list()
# new_list.random_num_list()

# Exc 3
class menu_manager:
    def __init__(self):
        self.menu=[
        { 'Soup' :10 ,'B' : False},
        {'Hamburger ': 15 , 'A':True},
        {'Salad ': 18 , 'A ': False},
        {'French Fries' : 5 ,'C ': False},
        {'Beef bourguignon': 25 , 'B' :True}
        ]
    def add_item(self ,name, price, spice, gluten):
        self.menu.append({name:price,spice:gluten})

    def update_item(self,name, price, spice, gluten):
        updated_item=''
        for i in range (len(self.menu)):
           if name in self.menu[i]:
            updated_item="update"
            self.menu[i]={name:price,spice:gluten}
            print(self.menu)
            print(f'{name} has been updated')
        if not updated_item:
            print("This Item is not on the menu")
        
    def remove_item(self,name):
        updated_item=''
        new_menu =self.menu
        for i in range (len(self.menu)):
           if name in new_menu[i]:
            updated_item="update"
            new_menu.remove(new_menu[i])
            print(self.menu)
      
        if not updated_item:
            print("This Item is not on the menu")
                        
chips=menu_manager()
chips.add_item('meat',10,'C',True)
print(chips.menu)
chips.update_item('Soup',25,'C',True)
chips.remove_item("Soup")