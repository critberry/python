'''''''''''''''''''''''''''
    A simple Tic Tac Toe
'''''''''''''''''''''''''''

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [ [' ' for x in range(0,self.size)] for y in range(0,self.size) ]

    def displayBoard(self):
        for row in self.grid:
            print(row)
            print('')

def checkWinCondition(board):
    # Check rows
    
    won = False
    for row in board.grid:
        matches = 0
        symbol = row[0]
        for block in row:
            if block == symbol and symbol != ' ':
                matches += 1
            if matches >= board.size:
                print('You won!')
                print('row')
                won = True
                break
        if won:
            break

    # Check columns
    
    for i in range(0, board.size):
        matches = 0
        symbol = board.grid[0][i]
        for k in range(0, board.size):
            if board.grid[k][i] == symbol and symbol != ' ':
                matches += 1
            if matches >= board.size:
                print('You won')
                print('column')
                won = True
                break
        if won:
            break

    # Check diagonal \
    
    m = 0
    n = 0
    matches = 0
    symbol = board.grid[0][0]
    while (m < board.size and n < board.size and not won):
        if (symbol == board.grid[m][n] and symbol != ' '):
            matches += 1
        if matches >= board.size:
            print('You won')
            print('diagonal \\')
            won = True
        m += 1
        n += 1

    # Check diagonal /
    
    m = 0
    n = board.size - 1
    matches = 0
    symbol = board.grid[0][board.size - 1]
    while (m < board.size and n >= 0):
        if (symbol == board.grid[m][n] and symbol != ' '):
            matches += 1
        if matches >= board.size:
            print('You won')
            print('diagonal /')
            won = True
        m += 1
        n -= 1

def displayMenu():
    pass

def main():
    board = Board(3)
    #board.grid[0][0] = 'X'
    board.grid[0][1] = 'X'
    board.grid[0][2] = 'O'
    #board.grid[2][1] = 'X'
    board.grid[1][1] = 'O'
    board.grid[2][2] = 'X'
    board.grid[2][0] = 'O'
    board.displayBoard()
    checkWinCondition(board)

if __name__ == '__main__':
    main()
