# Exc 1
# print (abs.__doc__)
# print(int.__doc__)
# def abs(number):
#     """Take the input value and return a positive number. A complex number will be returned as a positive number"""

#     pass

# Exc 2
class Money():
    def __init__ (self, currency, amount):
        self.amount = amount
        if amount >1:
            self.currency= currency +'s'
        else:
            self.currency= currency   
    def __str__ (self):
        return f'{self.amount} {self.currency}'

    def __int__ (self):
        return amount 

    def __repr__ (self):
        return f'{self.amount} {self.currency}'  

    # def __add__(self, number):
       
    #         if type(number) == int and self.currency==number.currency:
    #             total = self.amount + number
    #             try:
    #                 if self.currency==number.currency:
    #                     total= self.amount+number.amount
    #             except TypeError:
    #                 print('balg')        
    #             return total               
    #         elif  self.currency==number.currency:    
    #             total = self.amount + number.amount
    #             return total    
    # return total
#     def __iadd__(self,number):
#         total=self.amount+number.amount


# c1 = Money('dollar', 5)
# c2 = Money('dollar', 10)
# c4 = Money('shekel', 1)
# c3 = Money('shekel', 10)
# # print( str(c1))
# # print(c1 + 5)
# # print(c1 + c2)
# # print(c1)
# print(c1+c3)

# Exc 3
from datetime import datetime
def time_till_january():
    now=datetime.now()
    print('reef')
    print(datetime.now())
    print(f" January is in {(datetime(2022,1,1)-datetime.today()).days} days and {((datetime(2022,1,1)-datetime.now()).seconds/(60*60))} hours")
    
# Exc 4



# Exc 5
def life_time(day,month,year):
    today=datetime.today()
    life_minutes=datetime(year,month,day)
    total =today-life_minutes  
 
    print(f'you have been alive for {total}')
life_time(1,2,1994)

# Exc 6
seconds_in_earth_year=311557600
def age_in_seconds(age_seconds):
    e



