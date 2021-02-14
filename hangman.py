class HangMan:
    def __init__(self):
        self.hidden_word=''
        self.word_to_guess=''
        self.guessed_correct_letters=[]
        self.guessed_incorrect_letters=[]

    def choose_word(self):
        self.word_to_guess =input('PLayer 1 Choose a word ') 
        self.hidden_word=list('*'*(len(self.word_to_guess)))
        print("".join(self.hidden_word))

    def guess_word(self):
        guessed_letter=input('Player 2 choose a letter ')
        if guessed_letter in self.word_to_guess :
            self.guessed_correct_letters.append(guessed_letter)
            for i in range (len(self.word_to_guess)):
                if self.word_to_guess[i]==guessed_letter:
                  self.hidden_word[i]=guessed_letter                          
        else:
            self.guessed_incorrect_letters.append(guessed_letter)    
        print("".join(self.hidden_word))
        print( f'incorrectly gussed letters {self.guessed_incorrect_letters}')
        self.game_play()

    def game_play(self):
        if self.word_to_guess=='':
            self.choose_word()
        if '*' not in ''.join(self.hidden_word):
            print(f'You got the word:!!{"".join(self.hidden_word)}!!')
        elif  len(self.guessed_incorrect_letters)==10:
            print(f"Game over you used all 10 of you truns you didnt get the word ,the word is  {''.join (self.word_to_guess)}")
        else:
            self.guess_word()        

hang_man=HangMan()
hang_man.game_play()

