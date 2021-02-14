from itertools import permutations
class AnagramChecker:
    def __init__(self):
      with open('wordlist.txt',) as f:
        self.words=f.readlines()
        self.words2={ }

        for word in self.words:
            word=word.strip('\n')
            self.words2[word]=1

    def is_valid_word(self,word_choice):   
        x=" "
        if word_choice in self.words2:
            x='in'
        if x !='in':
            print('That is not a valid word') 

    def get_anagrams(self ,word_choice):
        anagrams=[ ]  
        for word in permutations(word_choice):
            word = "".join(word)
            if word in self.words2 and word!=word_choice:
                anagrams.append(word)
        if len(anagrams)==0:
            print('There are no anagrams for this word')
        else:            
            print(anagrams)        

    def game_play(self):
        word_choice=input("Choose a word ").upper()
        anagram1.is_valid_word(word_choice)
        anagram1.get_anagrams(word_choice)

anagram1=AnagramChecker()
anagram1.game_play()



