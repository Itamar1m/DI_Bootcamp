calc=[]
age =input('What date is your birthday DD/MM/YYYY')
year=2021-int(age[6:10])
month=2-int(age[3:5])
day=1-int(age[:2])
print(year)
candles=str(year)

if month <0 or day <0:
	
	candles=int(year)-1
else:
	candles=int(year)

candles=str(candles)
candles=candles[-1]	

letteri='i'*int(candles)	

print( f'     __  {letteri}  __ ' )
print('    |  :H:A:P:P:Y  |'   )     
print('   _|______________|_ ' )
print('  |^^^^^^^^^^^^^^^^^^|'  )
print('  | :B:i:r:t:h:d:a:y |'  )
print('  |                  |'  )
print('   ~~~~~~~~~~~~~~~~~~ '  ) 