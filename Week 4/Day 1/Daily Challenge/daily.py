# 1
string=input('Type in a few words ')


#2
if len(string)<10:
	print("String too short")
elif len(string)>10:
	print('String too long')
# 3
print(string[0],string[9]) 
# 4
empty=''
for x in range (0,len(string)):
	empty+=string[x]
	print(empty)
# 
import random
string=list(string)
shuffled=random.shuffle(string)

print(string)
print(.)