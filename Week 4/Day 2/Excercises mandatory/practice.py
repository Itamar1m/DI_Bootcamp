
# Exc 1
my_fav_numbers={0,1,2,3,4,5,6}
my_fav_numbers.add(7)
my_fav_numbers.add(8)
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)

# Exc 2
# no
# Exc 3
for x in range(1,21):
	print(x)
# Exc 4

numbers=[2,3,4,5]
floats =[1.5,2.5,3.5,4.5]
all_numbers=numbers+floats
print(all_numbers)
all_numbers.sort()
print(all_numbers)

# Exc 5
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.append('kiwi')
basket.insert(0,"Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

# EXC 6
# name=input('What is your name? ')
# while name!='itamar':
# 	name=input('What is your name? ')


# Exc 7
list =["Banana", "Apples", "Oranges", "Blueberries",'a','b']
for x in range(2,len(list),2):
	print(x)
	print(list[x])


# Exc 8
for x in range(3,30,3):
	print(x)

# Exc 9
for x in range(1500,2701,1):
	if x%7==0 and x%5==0:
		print(x)
#Exc 10

# fruits=input("Please type a fruit or number of fruits with a space between. ")
# fruits1=fruits.split()
# print(fruits1)
# choice=input("Please choose a fruit. ")
# if choice in fruits:
# 	print('You chose one of your favorite fruits! Enjoy!')
# else:
# 	print('You chose a new fruit. I hope you enjoy it too!')	

# if len(fruits1)==1:
# 	print(fruits)
# else:
# 	fruits1.insert(-1,'and')


#Exc 11
# Can do a while loop is better
# toppings=[]
# for x in range(500):
# 	selection=input("Select a topping for your pizza ")
# 	if selection == 'quit':
# 		toppings="".join(toppings)
# 		price=(len(toppings)-1)*2.5
# 		print(f'These are your toppings {toppings} the cost is ${price+10}')
# 		break
# 	else:
# 		toppings.append(selection)
# 		print(f'Youll add {toppings} to your pizza. ')

# Exc 12 part1
people=[]
prices=input('Tell me your ages  ')
prices=prices.split()
prices=[int(i) for i in prices]
print(prices[0])
for i in range(0,len(prices)):
	if prices[i]>3 and  prices[i] <=12:
		people.append(10)
		print(people)
	elif  prices[i]>12:
		people.append(15)

print(prices)
total_cost=sum(people)

print('the cost is $'+ str(total_cost))

# Exc 12 part 2
# allowed=[]
# for i in range(2) :
# 	name =input("What is your name? ")
# 	ages =input("How old are you? ")
# if int(ages)<16 or int(ages)>21:
# 	allowed.append(name)

# allowed="".join(allowed)
# print(allowed+' can see the movie')

# # Exc 13
# users =["ben","dan","rik","lis","sam","jon"]

# for i in range(0,len(users)):
# 	 age =input(f'{users[i]} how old are you? ')
# 	 age=int(age)
# 	 if age<16:
# 	 	users[i]='x'

# users=set(users)
# users.remove('x')
# print(users)	 	

# Exc 14
added_names=[]
while True:
	option=input('Please choose an option: a) Add Name b)Remove name c)View family members d)Exit')
	if option=='a':
		add_name=input("Type the name ou want to add. ")
		added_names.append(add_name)
	elif option=='b':
		if len(added_names)==0:
			print('No names to remove')
		else:
			remove_name=input('what name would you like to remove? ')
			added_names.remove(remove_name)
	elif option=='c':
		print(added_names)
	elif option=='d':
		print('Goodbye')
		break






	
	
	











