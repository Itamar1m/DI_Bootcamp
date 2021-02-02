# Exc 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
num=zip(keys,values)
ans=dict(num)

print(ans)
print(type(ans))

# Exc 2
family = {
"rick": 43, 
'beth': 13, 
'morty': 5, 
'summer': 8}

total_cost=[]
price_list=family.items()
print(price_list)
for i in price_list:
	if i[1] >3 and i[1] <=12:
		total_cost.append(10)
		print(f'{i[0]} will cost $10')
	elif i[1]>12:
		total_cost.append(15)
		print(f'{i[0]} will cost $15')  	

print(f'total cost is ${sum(total_cost)}')

# Exc 3
brand={
'name':'Zara' ,
'creation_date': 1975 ,
'creator_name': 'Amancio Ortega Gaona' ,
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'type_of_clothes': ['men', 'women', 'children', 'home'] ,
'number_stores': 7000 ,
'major_color':{'France': 'blue',' Spain' : 'red', 'US' : ['pink', 'green']} 
}

brand['number_stores']=2
brand['country_creation']='Spain'
brand['international_competitors'].append('Desigual')
print(brand['international_competitors'])
del brand['creation_date']
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())

more_on_zara={
'creation_date': 1975 ,
'number_stores': 10000 

}
brand.update(more_on_zara)
print(brand['number_stores'])#The last number stores is removed.

 #Exc 4
first_result={}
second_result={}
third_result={}
final={}
final1={}
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"] 
for i in range(0,len(users)):
	second_result[i]=users[i]

print(second_result)

for i in users:
	first_result[i]=users.index(i)

print(first_result)	

users.sort()

for i in users:
	third_result[i]=users.index(i)

print(third_result)	

# num 4
for i in users:
	if 'i' in i:
		final[i]=users.index(i)

print(final)	

for i in users:
	if i[0:1]=='M' or  i[0:1]=='P':	
		final1[i]=users.index(i)

print(final1)
