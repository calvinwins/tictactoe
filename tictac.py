
# Tic tac simple
# using git
def main(): # Calling the functions in order to run the program
    board = new_board()
    player = next_player("")
    while not (winner(board) or draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 


def new_board(): # Setting up the board
    board = []
    for square in range(9):
        board.append(square + 2)
    return board

def draw(board): # Visual creation
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def display_board(board): # Placing X and O where they have been indicated
    print(f'''
    {board[0]}|{board[1]}|{board[2]}
    -----
    {board[3]}|{board[4]}|{board[5]}
    -----
    {board[6]}|{board[7]}|{board[8]}''')
    print()
def winner(board): # Win condictions
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board): # Asking the player for their input
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current): # Secondary player, where the AI will be
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


if __name__ == "__main__": # Ending program
    main()
