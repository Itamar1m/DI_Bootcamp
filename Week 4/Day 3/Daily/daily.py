text =input('Would you like to encrypt or decrypt')
word=input('Type in a word')
encryption=''
for i in word:
	if text=='encrypt':
		encryption +=chr((ord(i)-3))
	elif  text=='decrypt':
		encryption+=chr((ord(i)+3))
		

print(encryption)