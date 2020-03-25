'''''''''''''''''''''''''''
    A simple Tic Tac Toe
'''''''''''''''''''''''''''

class Board:
    def __init__(self, size, player):
        self.size = size
        self.grid = [ [' ' for x in range(0,self.size)] for y in range(0,self.size) ]
        self.current_player = player

    def displayBoard(self):
        row_number = 0
        column_number = ''
        for i in range(0,self.size):
            column_number += str(i) + (' ')
        print('  ' + column_number)
        for row in self.grid:
            row_temp = ""
            for symbol in row:
                if symbol == " ":
                    row_temp += "_ "
                else:
                    row_temp += symbol + " "
            print(str(row_number) + ' ' + row_temp)
            row_number += 1

    def checkWinCondition(self):
        # Check rows
        # player = 'X' oder 'O'

        if [self.current_player]*self.size in self.grid:
            return True
        

        # Check columns
        for j in range(self.size):
            if [self.grid[i][j] for i in range(self.size)] == [self.current_player]*self.size:
                return True

        # Check diagonal \
        if [self.grid[i][i] for i in range(self.size)] == [self.current_player]*self.size or \
            [self.grid[self.size-1-i][i] for i in range(self.size)] == [self.current_player]*self.size:
            return True
        
        return False

    def checkMove(self, x, y):
        if x >= self.size or y >= self.size:
            return False
        return self.grid[x][y] == ' '

    def move(self, x, y):
        self.grid[x][y] = self.current_player

    def displayMenu(self):
        print('')
        print('Current player: ' + self.current_player)
        print('M - Make a move')
        print('Q - Quit')

    def switchPlayer(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

def main():
    player = 'X'
    size = 3
    board = Board(size, player)

    game_over = False

    while (not game_over):
        print('===============================')
        board.displayBoard()
        board.displayMenu()
        key = input('Choose an option: ')
        key = key.upper()
        if key == 'M':
            digits = ''
            while (not digits.isdigit() or len(digits) != 2):
                digits = input('Enter two digits e.q. 01: ')
            x = int(digits[0])
            y = int(digits[1])
            if board.checkMove(x,y):
                board.move(x,y)
                game_over = board.checkWinCondition()
                if (not game_over):
                    board.switchPlayer()
                else:
                    board.displayBoard()
                    print('Player ' + board.current_player + ' has won!')
            else:
                print('Field is either occupied or out of bounce.')
        elif key == 'Q':
            print('Good bye..')
            game_over = True
        else:
            print('Invalid input. Please try again.')
        

if __name__ == '__main__':
    main()
