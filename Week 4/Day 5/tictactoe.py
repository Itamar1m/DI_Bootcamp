
board = [
 [' ' ,' ' ,' '],
 [' ' ,' ' ,' '],
 [' ' ,' ' ,' ']
]

def display_board():

    print(f'{ board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('--|---|--')
    print(f'{ board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('--|---|--')
    print(f'{ board[2][0]} | {board[2][1]} | {board[2][2]} ')

def player1_turn():
    print("Player 1's turn:")
    user_input_col = int(input('select col: '))
    user_input_row = int(input('select row: '))
    if board[user_input_row][user_input_col] != ' ':
        print('invalid move try again.')
        player1_turn()  
    else:
        board[user_input_col][user_input_row] = 'x'

def player2_turn():
    print("Player 2's turn:")
    user_input_col = int(input('select col: '))
    user_input_row = int(input('select row: '))
    if board[user_input_col][user_input_row] != ' ':
                print('invalid move try again.')
                player2_turn()
    else:
        board[user_input_col][user_input_row] = 'o'

def end_of_game():
    if board[0][0] and board[0][1] and board[0][2] and board[1][0] and board[1][1] and board[1][2] and board[2][0] and board[2][1] and board[2][2] != ' ':
        return True
        

def game_play():
    while True:
        display_board()      
        if end_of_game():
            display_board()
            print("Game over!")
            break        
        else:
            player1_turn()
        if end_of_game():
            display_board()
            print("Game over!")
            break
        else:
            display_board()
            player2_turn()
game_play()    







# def display_board():
#     for i in board:
#          print("".join(i))
#     # print(" ".join(row1))
#     # print('--|---|--')
#     # print(" ".join(row2))
#     # print('--|---|--')
#     # print(" ".join(row3))   
# display_board()

# # def player1_turn():   
# #     print('Player 1"s turn.... ')    
# #     player1_row=input('Enter row: ')
# #     player1_column=input('Enter column: ')
# #     if player1_row=='1' :
# #             if player1_column =='3'and row1[4]==False:
# #                 row1[4]='x'
# #             elif player1_column=='2'and row1[2:3]!='o':
# #                 row1[2:3]='x'
# #             elif player1_column=='1'and row1[0:1]!='o':
# #                 row1[0:1]='x'
               
# #     elif player1_row=='2' :
# #             if player1_column =='3'and row1[4]!='o':
# #                 row2[4]='x'
# #             elif player1_column=='2'and row1[2:3]!='o':
# #                 row2[2:3]='x'
# #             elif player1_column=='1'and row1[0:1]!='o':
# #                 row2[0:1]='x'
               
# #     elif      player1_row=='3' :
# #             if player1_column =='3'and row1[4]!='o':
# #                 row3[4]='x'
# #             elif player1_column=='2'and row1[2:3]!='o':
# #                 row3[2:3]='x'
# #             elif player1_column=='1'and row1[0:1]!='o':
# #                 row3[0:1]='x'
     
           
# # def player2_turn():
# #     print('Player 2"s turn....')    
# #     player2_row=input('Enter row: ')
# #     player2_column=input('Enter column: ')
# #     if player2_row=='1' :
# #         if player2_column =='3' and row1[4]!='x':
# #             row1[4]='o'
# #         elif player2_column=='2'and row1[2:3]!='x':
# #             row1[2:3]='o'
# #         elif player2_column=='1'and row1[0:1]!='x':
# #             row1[0:1]='o'

# #     elif player2_row=='2' :
# #             if player2_column =='3'and row1[4]!='x':
# #                 row2[4]='o'
# #             elif player2_column=='2'and row1[2:3]!='x':
# #                 row2[2:3]='o'
# #             elif player2_column=='1'and row1[0:1]!='x':
# #                 row2[0:1]='o'

# #     elif player2_row=='3' :
# #             if player2_column =='3'and row1[4]!='x' :
# #                 row3[4]='o'
# #             elif player2_column=='2'and row1[2:3]!='x':
# #                 row3[2:3]='o'
# #             elif player2_column=='1'and row1[0:1]!='x':
# #                 row3[0:1]='o'           
  
# #  def end_of_game():
# #     win_conditions=[
# #         [row1[0],row1[1], row1[2]], 
# #         [row2[0],row2[1],row2[2]],
# #         [row3[0],row3[1],row3[2]]
# #         ]
# #     for win_condition in win_conditions:
# #         if win_condition:
# #             print('Game over')
# #             return True
        

# # def game_play():  
# #     display_board()
# #     while True:
# #         if end_of_game():
# #             break:
# #         else:   
# #             player1_turn()
# #             display_board()
# #             player2_turn()
# #             display_board()


      
# # game_play()
