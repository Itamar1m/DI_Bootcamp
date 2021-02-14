
Exc 1
import random
def get_words_from_file():
    with open('wordlist.txt',) as f:
        words =f.readlines()
    return words    

def get_random_sentence(length):
    words=get_words_from_file()
    random_words=random.choices(words,k=length)
    random_sentence=' '
    for  word in  random_words:
        word=word.strip('\n')
        random_sentence += f'{word} ' 
    print(random_sentence)
    return random_sentence   
   
def main():
    print("This is a random sentence generator:")   
    sentence_length=input("How long do you want your sentence to be?(2-20) ")
    if  type(sentence_length)!= int or  sentence_length <2 or  sentence_length >20 :
        print("Invalid input")
    else:
        get_random_sentence(sentence_length)    
main()
    
Exc 2
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
json_test=json.loads(sampleJson)
print(json_test['company']['employee']['payable']['salary'])
json_test['company']['employee']['birth_date']= '10/01/1994'
print(json_test)

with  open('jsonnne_test.txt', 'w') as f:
    # json.dump(json_test,f)
    f.write(json.dumps(json_test))



