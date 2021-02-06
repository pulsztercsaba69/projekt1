board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
    print(board[0] + " I " + board[1] + " I " + board[2])
    print(board[3] + " I " + board[4] + " I " + board[5])
    print(board[6] + " I " + board[7] + " I " + board[8])

def play_game():

    #display initial board
    display_board()


    handle_turn()


def handle_turn():
    position = input("Válassz egy számot 1 és 9 között:  ")

play_game()









#board
#display board
#play game
#handle turn
#check win
 #check rows
 #check columns
 #check diagonals
#check tie
#flip player