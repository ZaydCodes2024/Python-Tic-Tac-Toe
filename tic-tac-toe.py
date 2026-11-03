
def new_board():
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

board = new_board()

def render(board):
    row_count = 0
    print('  0 1 2')
    print('  ------ ')
    for row in board:
        print('%s|' %row_count, end='')
        row_count += 1
        print(' '.join([' ' if cell is None else cell for cell in row]), end='')
        print('|')
    print('  ------ ')

render(board)

def get_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None
   

def get_move():
    print("Enter the coordinates of your move (x,y)")
    x = input('Enter your move (x): ')
    y = input('Enter your move (y): ')
    return tuple(map(int, (x, y)))

def is_valid_move(board, move_coords):
    x, y = move_coords
    try:
        if board[x][y] == ' ' and 0 <= x < 3 and 0 <= y < 3:
            return True
    except IndexError:
        return False
    
    return False

def make_move(board, move_coords, player):
    while True:
        move_coords = get_move()
        x, y = move_coords
        if not is_valid_move(board, move_coords):
            print("Invalid move. Try again.")
            continue
        board[x][y] = player
        return board

move_coords1 = None

board = make_move(board, move_coords1, 'X')

move_coords2 = None

board = make_move(board, move_coords2, 'O')

render(board)