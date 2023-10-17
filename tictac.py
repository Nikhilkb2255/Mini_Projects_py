from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7] +"|"+ board[8] +"|"+ board[9])
    print(board[4] +"|"+ board[5] +"|"+ board[6])
    print(board[1] +"|"+ board[2] +"|"+ board[3])
    
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("\nPlayer 1 - Choose X or O : ").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
# player_1, player_2 = player_input()

def place_marker(board, position, marker):
    board[position] = marker

# place_marker(test_board, 8, '$')
# display_board(test_board)

def win_check(board,marker):
    return ((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[7] == board[4] == board[1] == marker) or
    (board[8] == board[5] == board[2] == marker) or
    (board[9] == board[6] == board[3] == marker) or
    (board[1] == board[5] == board[9] == marker) or
    (board[7] == board[5] == board[3] == marker))
    
# display_board(test_board)
# win_check(test_board,'X')

import random
def choose_first():
    toss = random.randint(0,1)
    if toss == '0':
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board,position):
    return board[position] == ' '

def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    pos = 0
    while pos not in range(1,10) or not space_check(board,pos):
        pos = int(input("\nChoose a position(1-9): "))
    return pos

def reply():
    choice = input("\nDo u wish 2 continue(y/n): ")
    return choice == 'y'

print("Welcome to th game !")

while True:
    the_board = [' ']*10
    player_1, player_2 = player_input()

    turn = choose_first()
    print("\nRandomly "+turn+" gonna play first..")

    play_game = input("\nAre u ready?(y/n)").lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player_1':
            
            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, position, player_1)

            if win_check(the_board,player_1):
                display_board(the_board)
                print("\nPlayer 1 has won !")
                game_on = False
            elif full_check(the_board):
                display_board(the_board)
                print("\nIt's a tie !")
                game_on = False
            else:
                turn = 'player_2'
                            
        else:
            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, position, player_2)

            if win_check(the_board,player_2):
                display_board(the_board)
                print("\nPlayer 2 has won !")
                game_on = False
            
            elif full_check(the_board):
                display_board(the_board)
                print("\nIt's a tie !")
                game_on = False
            
            else:
                turn = 'player_1'
  
    if not reply():
        break
