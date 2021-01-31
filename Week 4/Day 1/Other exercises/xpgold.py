# Exc 1
print('hello world\n'*5+'I love python\n'*4)
# Exc 2
month=input('Give me a month (1-12) ')
month=int(month)

if month==0 or month>12:
	print('Not a number between 1 and 12')	
elif month>=3 and month<=5:
	print('Its spring')
elif month>=6 and month<=8:
	print('Its summer')
elif month>=9 and month<=11:
	print('Its Autumn')
else:
	print('Its winter')


# xpNinja
# Exc 3
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Exc 4
text="Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamcolaboris nisi ut aliquip ex ea commodo consequat.  aute irure dolor in reprehenderit in voluptate velit Excepteur sint occaecat cupidatat non proident,"
print(len(text))

# Exc 5
sentence = input("Give me the longest sentence you can without the letter A ")
print(len(sentence))
a_less = ["r"]


def sen():
    sentence = input("Give me the longest sentence you can without the letter A ")
    func()

    return sentence


sent = sen()


def func():
	if 'a' not in sent :

	    a_less.append(sent)
	elif len(a_less[1])<len(a_less[0]) and 'a' not in sent:
		print('Well done thats your biggest a_less sentence')
	sen()
	return
	# elif len(a_less) == 1 and 'a' not in sent:
	#     print('Well done thats your biggest a_less sentence')
	# # sen()
	# else:          
	# 	print('There is an a in your sentence')
	# return	
sen()


  
sen()


