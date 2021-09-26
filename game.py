# Tic Tac Toe class + game implementation by me
# try to defeat the computer 
# non copyrighted
# seeked help from a youtuber T_T
# music i listen to while i code https://open.spotify.com/playlist/0eZuvCrua6GSTnUlimORoQ?si=75890dd981d841c9


import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe(): #we created a class tictactoe
    def __init__(self): #we initialized it
        self.board = self.make_board() #we have created a board
        self.current_winner = None #we initialized a current winner to none

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)] #we returned a board to the length 9

    def print_board(self): # creating and printing 3 rows
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            # visual purposes only

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter): #we actually make moves on this board
    # space where user can go freely | letter represents users 'x' or 'o' move
        if self.board[square] == ' ': # empty space so that user can assign a value
            self.board[square] = letter # assign a letter 'x' or 'o'
            if self.winner(square, letter): # check to see the winner
                self.current_winner = letter # value is assigned to the current player if he's the winner
            return True
        return False

    def winner(self, square, letter): #checking if the move is making user a winner
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        # taking a letter first and assigning it in the row, if it's true then we return true
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        # same thing we did in row can be applied here, we check if the value is true and we return true
        if square % 2 == 0: # we are checking if the square is even
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # we are checking if the values are same
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # we are checking if the values are same
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]): # if the values are same we return it true other wise false
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    # tells the user how if there are any empty squares

    def num_empty_squares(self):
        return self.board.count(' ')

    # tells the user exact number of empty squares or counts the empty squares

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
    # gives the value of remaining empty spaces


def play(game, x_player, o_player, print_game=True): # we define play which has game, x player and o player and print game

    if print_game:
        game.print_board_nums()

    letter = 'X' # x is always first idk why
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game) # if o player is next it takes the value of o otherwise
        else:
            square = x_player.get_move(game) # x player gets his chance
        if game.make_move(square, letter): # we used if statement because we want to check if its a valid move or not

            if print_game: # if its true
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner: # we check and print if its true
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

# ~.....   end of code .....~

