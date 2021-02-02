# XP Gold
# exc 1-3
# birthdays={
#     'a':  '1994/09/04',
#     'b':  '2000/09/07',
#     'c':  '1982/21/11',
#     'd':  '1992/02/22',
#     'e':  '2008/03/015', 
# }
# user_name=input('What is your name? ')
# userbday=input('Please tell us your birthday in the following format:YYYY/MM/DD ')
# birthdays[user_name]=userbday

# list_names=birthdays.keys()
# list_names=list(list_names)
# list_names=''.join(list_names)

# print(f'Hello you can look up {list_names}  birthday ')
# person =input('Whos birthday would you like to look up? ')
# if person in list_names:
#     print(f" {person}'s birthday is on {birthdays[person]} ")
# else:
#     print(f'Sorry, we don’t have birthday information for {person}')

# Exc 4
items={
"banana": {'price':4,'stock' :10 },
"apple": {'price':2,'stock':25 },
"orange": {'price':1.5 ,'stock':12 },
"pear": {'price':3,'stock':5 },
}
cost=[]
loop=items.items()
print(loop)
for i in loop:
    total_stock_cost=i[1]['price']*i[1]['stock']
    cost.append(total_stock_cost)

print(cost)

print(sum(cost))

# Exc 5
car_string='Volkswagen, Toyota, Ford Motor, Honda, Chevrolet'
car_list=car_string.split()
print(car_list)
print(f'There are {len(car_list)} manufacturers')
car_list.sort()
car_list.reverse()
print(car_list)

# How many have the letter o
o_list=[]
i_list=[]
for i in car_list:
    if 'o' in i:
        o_list.append(1)
    if 'i' not in i:
        i_list.append(1)

print(f"i's {sum(i_list)}")
print(f"o's {sum(o_list)}")

# Bonus
list_cars= ['Honda','Volkswagen', 'Toyota', 'Ford Motor', 'Honda','Chevrolet', 'Toyota']
set_cars=set(list_cars)
print(set_cars)
set_cars=list(set_cars)

# set_cars=' '.join(set_cars)
# set_cars=set_cars.split(',')

set_cars=sorted(set_cars)
back_carlist=[ i[::-1] for i in car_list]
# for i in set_cars:
#     i=i[::-1]
#     print(i)

print(back_carlist)