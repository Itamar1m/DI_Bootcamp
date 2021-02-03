# Exc 1
import random

# def get_random_temp(season):
#     if season=='summer':
#         random_temp=random.randint(20.0,40.0)
#     elif season =='winter':
#         random_temp=random.randint(-10.0,10.0)

#     random_temp=float(random_temp)
#     return random_temp
    
# def main():
#     tempreature=get_random_temp( input('what seson is it? '))
#     if tempreature<0:
#         print(f'The tempreature now is {tempreature} degrees Celcius, Its freezing!')
#     elif tempreature>=0 and tempreature <16:
#         print(f'The tempreature now is {tempreature} degrees Celcius,Don’t forget your coat!')
#     elif tempreature>=16 and tempreature <23:
#             print(f'The tempreature now is {tempreature} degrees Celcius,Looks like a nice day!')
#     else:
#         print(f'The tempreature now is {tempreature} degrees Celcius,its a bit warm out!')
# main()

# Exc 2
def throw_dice():
   dice_a= random.randint(1,6)
   dice_b=random.randint(1,6)
   return dice_a,dice_b

throws=[]

def throw_until_doubles():
        while True:
            throw_dice()
            die=throw_dice()
            throws.append(1)
            if  die[0]!=die[1]:
                throws.append(1)                    
            else:
                print(len(throws))
                break 


def main():
    doubles=[]
    while True:
        throw_until_doubles()
        doubles.append(throws)
        if len(doubles)==100:
            print(len(doubles))
            break
    print(f'Total throws: {len(throws)}')
    amount=float(len(throws))
    print(f'Average throws per double: {amount/100}')    
main()            


    
