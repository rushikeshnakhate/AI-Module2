import easyAI as e

print(help(e))
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']
         ]


def players(board):
    x_count = 0
    y_count = 0
    for row in board:
        for column in row:
            if column == 'X':
                x_count += 1
            elif column == 'O':
                y_count += 1
    if x_count == y_count:
        return 'X'
    else:
        return 'O'


def action(board):
    moves = []
    for r, row in enumerate(board):
        for c, val in enumerate(board):
            if val == '':
                print(r, c)
                moves.append((r, c))
    return set(moves)


def column_winners(board):
    '''Returns "X" or "O" or None according to whether either one of the players
    has achieved three symbols in a vertical column.'''
    ###
    ### YOUR CODE HERE
    ###
    number_of_row = len(board)
    number_of_col = len(board[0])

    for c in range(number_of_col):
        x_count = 0
        o_count = 0
        for r in range(number_of_row):
            if board[r][r] == 'X':
                x_count += 1
            if board[c][r] == 'O':
                o_count += 1

            if x_count > 2:
                return 'X'
            elif o_count > 2:
                return 'O'
    return None


board_1 = [['X', 'X', 'O'],
           ['X', 'X', 'O'],
           ['X', 'O', '']]


## GRADED
### QUESTION 18
def diagonal_winners(board):
    '''Returns "X" or "O" or None according to whether either one of the players
    has achieved three symbols in sequence along either diagonal.'''
    ###
    ### YOUR CODE HERE
    ###
    number_of_row = len(board)
    number_of_column = len(board)
    r = 0
    c = 0
    while r < number_of_row:
        x_count = 0
        o_count = 0
        while c < number_of_column:
            if board[r][c] == 'X':
                x_count += 1
            elif board[r][c] == 'O':
                o_count += 1
            if x_count > 2:
                return 'X'
            if o_count > 2:
                return 'O'
            c = c + 1
            r = r + 1

    if (x_count < 3) and (o_count < 3):
        r = 2
        c = 0
        while r > -1:
            x_count = 0
            o_count = 0
            while c < number_of_column:
                if board[r][c] == 'X':
                    x_count += 1
                elif board[r][c] == 'O':
                    o_count += 1
                if x_count > 2:
                    return 'X'
                if o_count > 2:
                    return 'O'
                c = c + 1
                r = r - 1

    return None


board_1 = [['O', '', 'X'],
           ['O', 'X', 'O'],
           ['X', 'X', 'X']]
print(diagonal_winners(board_1))
