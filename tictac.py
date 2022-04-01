# Calvin Weaver
# Tic tac toe
# using git
def main():
    print('Tic Tac Toe')
    board = new_board()
    player = next_player("")
    while not (winner(board) or draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    if draw(board):
        print('Tie Game!')
    elif winner(board, 'o'):
        print('The Machine Won')
    else:
        print("You Won! Thanks for playing!") 


def new_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def display_board(board):
    print(f'''
    {board[0]}|{board[1]}|{board[2]}
    -----
    {board[3]}|{board[4]}|{board[5]}
    -----
    {board[6]}|{board[7]}|{board[8]}''')
    print()
def winner(board, le):
    return (board[0] == le and board[1] == le and board[2] == le or
            board[3] == le and board[4] == le and board[5] == le or
            board[6] == le and board[7] == le and board[8] == le or
            board[0] == le and board[3] == le and board[6] == le or
            board[1] == le and board[4] == le and board[7] == le or
            board[2] == le and board[5] == le and board[8] == le or
            board[0] == le and board[4] == le and board[8] == le or
            board[2] == le and board[4] == le and board[6] == le)

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player



def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


if __name__ == "__main__":
    main()

