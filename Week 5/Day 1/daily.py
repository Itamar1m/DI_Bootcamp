
class Farm:
    def __init__(self,farm_name):
        self.farm_name=farm_name
        self.dict_amount_animal={}

        """Adds animals and there amount"""
    def add_animal(self,animal ,amount=1):
        if animal not in self.dict_amount_animal:
            self.dict_amount_animal[animal] =amount
        else:
             self.dict_amount_animal[animal] += amount

    """ Prints it out neatly """
    def get_info(self): 
        print("Macdonald's farm")  
        for item in self.dict_amount_animal.items():
            print(f'{item[0]}: {item[1]}')

    def get_animal_types(self):
       list_of_animals=list(self.dict_amount_animal.keys())
       print(list_of_animals)
       return list_of_animals
  

    def get_short_info(self):
        short_info_list=macdonald.get_animal_types()
        items_to_join=(short_info_list[0:len(short_info_list)-1])
        joined_list= ",".join(items_to_join)
        print(f'Macdonalds farm has {joined_list} and {short_info_list[-1]}.')
    

macdonald=Farm('macdonald')
macdonald.add_animal('sheep',5)
macdonald.add_animal('goat')
macdonald.add_animal('cow',2)
macdonald.add_animal('oxen',7)
macdonald.add_animal('oxen')
macdonald.get_animal_types()
macdonald.get_info()
macdonald.get_short_info()

