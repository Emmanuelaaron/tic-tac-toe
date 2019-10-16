#board
board =  ["-", "-", "-", "-", "-", "-","-", "-", "-"]

game_on_going = True

winner = None

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display_board()

    while game_on_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won")
    elif winner == None:
        print("Tie")

def handle_turn(Player):
    position = input("choose a position from 1-9: ")
    position = int(position) - 1
    board[position] = "X"
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    #check rows
    row_winner = check_rows()

    #check Columns
    column_winner = check_columns()
    #check diagonals
    if row_winner:
        winner = row_winner
    if column_winner:
        winner = column_winner

def check_if_tie():
    return

def check_rows():
    global game_on_going
    if board[0] == board[1] == board[2] != "-":
        game_on_going = False
        return board[0]
    if board[3] == board[4] == board[5] != "-":
        game_on_going = False
        return board[3]
    if board[6] == board[7] == board[8] != "-":
        game_on_going = False
        return board[6]

def check_columns():
    global game_on_going
    if board[0] == board[3] == board[6] != "-":
        game_on_going = False
        return board[0]
    if board[1] == board[4] == board[7] != "-":
        game_on_going = False
        return board[1]
    if board[2] == board[5] == board[8] != "-":
        game_on_going = False
        return board[2]
    return
def flip_player():
    return
play_game()
