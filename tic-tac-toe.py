"""Sets the game board."""
game_board={ '7': ' ' , '8': ' ' , '9': ' ' ,
             '4': ' ' , '5': ' ' , '6': ' ',
             '1': ' ' , '2': ' ' , '3': ' ' }

board_keys=[]

for key in game_board:
    board_keys.append(key)

"""Prints the board out everytime the function is called.
"""
def showBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')

"""Main function for gameplay"""

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        showBoard(game_board)
        print("Its your go," + turn +',' "Choose wisely!")

        move=input()
        if game_board[move] == ' ':
            game_board[move] = turn

            count += 1



if __name__ == '__main__':
    game()