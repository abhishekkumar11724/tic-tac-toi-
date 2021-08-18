row1=[1,2,3]
row2=[4,5,6]
row3=[7,8,9]
player_1='O'
player_2='X'

from os import system

def display_v():
    clear = lambda : system('cls')
    clear()
    print('the status of the game board is : ')
    print(f'{row1[0]} | {row1[1]} | {row1[2]}')
    # print('__________')
    print(f'{row2[0]} | {row2[1]} | {row2[2]}')
    # print('__________')
    print(f'{row3[0]} | {row3[1]} | {row3[2]}')
    
def input_v(player):
    choice='string'
    place_taken=False
    while choice.isdigit()==False or int(choice) not in range(1,10) or place_taken == False:
        choice=input('enter the digit corrosponding to the board :')
        if choice.isdigit()==False:
            print('oops! please enter a digit (1-9)...')
        if choice.isdigit()==True:
            if int(choice) not in range(1,10):
                print('oops! out of range(1-9)')
        if choice.isdigit()==True and int(choice) in range(1,10):
            if 1 <= int(choice) <= 3 :
                if row1[int(choice)-1]=='O' or row1[int(choice)-1]=='X' :
                    print('sorry! the block is taken...')
                else:
                    place_taken=True
            elif 4 <= int(choice) <= 6 :
                if row2[int(choice)-4]=='O' or row2[int(choice)-4]=='X' :
                    print('sorry! the block is taken...')
                else:
                    place_taken=True
            else:
                if row3[int(choice)-7]=='O' or row3[int(choice)-7]=='X' :
                    print('sorry! the block is taken...')
                else:
                    place_taken=True
            
    return int(choice)

def check_v(choice,player):    
    if 1 <= choice <= 3 :
        if player=='O':
            row1[choice-1]=player
        else:
            row1[choice-1]=player
    elif 4 <= choice <= 6 :
        if player=='O':
            row2[choice-4]=player
        else:
            row2[choice-4]=player
    else:
        if player=='O':
            row3[choice-7]=player
        else:
            row3[choice-7]=player
    # clear = lambda : system('cls')
    # clear()

def logic_g():
    c_game = True
    if row1[0]==row1[1]==row1[2]:
        if row1[0]=='X':
            print('player 2 has won the game!')
            c_game=False
        else:
            print('player 1 has won the game!')
            c_game=False
    if row2[0]==row2[1]==row2[2]:
        if row3[0]=='X':
            print('player 2 has won the game!')
            c_game=False
        else:
            print('player 1 has won the game!')
            c_game=False
    if row3[0]==row3[1]==row3[2]:
        if row3[0]=='X':
            print('player 2 has won the game!')
            c_game=False
        else:
            print('player 1 has won the game!')
            c_game=False
    if row1[0]==row2[0]==row3[0]:
        if row1[0]=='X':
            print('player 2 has won the game!')
            c_game=False
        else:
            print('player 1 has won the game!')
            c_game=False
    if row1[1]==row2[1]==row3[1]:
        if row1[1]=='X':
            print('player 2 has won the game!')
            c_game=False
        else:
            print('player 1 has won the game!')
            c_game=False
    if row1[2]==row2[2]==row3[2]:
        if row1[0]=='X':
            print('player 2 has won the game!')
            c_game=False
        else:
            print('player 1 has won the game!')
            c_game=False
    if row1[0]==row2[1]==row3[2]:
        if row1[0]=='X':
            print('player 2 has won the game!')
            c_game=False
        else:
            print('player 1 has won the game!')
            c_game=False
    if row3[0]==row1[1]==row1[2]:
        if row1[0]=='X':
            print('player 2 has won the game!')
            c_game=False
        else:
            print('player 1 has won the game!')
            c_game=False
    return c_game

while True:
    display_v()
    print('player 1 turn : ')
    choice=input_v(player_1)
    check_v(choice,player_1)
    game=logic_g()
    if game==False:
        break
    display_v()
    print('player 2 turn : ')
    choice=input_v(player_2)
    check_v(choice,player_2)
    game=logic_g()
    if game == False:
        break
