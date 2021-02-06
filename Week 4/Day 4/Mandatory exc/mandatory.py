# Exc 1
def display_msg():
    print('We are learning python. ')

display_msg()       

# # Exc 2
def favorite_book(title):
    print(f'My favourite book is {title}.')
favorite_book('Harry Potter')

# Exc 3
def describe_city(city,country='Israel'):
    print(f'{city} is in {country}')
describe_city('Jerusalem')
describe_city('Joburg','South Africa')

# Exc 4
import random 
def guess_num(num):
    random_num=random.randint(0,100)
    print(random_num)
    if num>100 or num <0:
        print('That number is out of range.')
    elif num ==random_num:
        print('You got it!')
    else:
        print(f'You failed your num was {num} the other was {random_num} ')    

guess_num(88)        

Exc 5
def  make_shirt(size="L",text="I love Python"):

  else:
      print(f"The shirts size is {size} and '{text}' should be printed on it.")

make_shirt(L,'Hello')
make_shirt(text='Hello',size=7)



Exc 6
magicians=['adam','harry','david','jim']
def show_magicians():
    for i in magicians:
        print(i)

def make_great():
    for i in range (len(magicians)):
        magicians[i]=magicians[i]+' the great'

make_great()
show_magicians()

# Exc 7
current_year=2021
current_month=2
current_day=3
def get_age(year, month,day=0):
    month =int(month)
    day  =int(day)
    year =int(year)
    if current_month-month<0:
        current_age=current_year-year-1
        print(current_age)        
      
    else:    
        current_age =current_year-year
        print(current_age)     
    return current_age

# get_age(1900,1)

def can_retire(gender,date_of_birth):
    year,month,day=date_of_birth.split('/')
    # Put the int in these brackets instead of in the first function better.(int(year)etc...)
    retirable=get_age(year,month,day)

    if gender=='male' and retirable >67:
        print(True)
    elif gender=='female' and retirable >62 :
        print(True)
    else:
        print(False)     

can_retire('male','1991/1/1')

# Exc 8
def x(integer):
    integer=str(integer)
    int1=integer*2
    int2=integer*3
    int3=integer*4
    answer=int(integer)+int(int1)+int(int2)+int(int3)
    print(answer)
 
x(3)

