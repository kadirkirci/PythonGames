# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:22:50 2022

@author: Kadir
"""
import time
from player import HumanPlayer, RandomComputerPlayer,GeniusComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None
        
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        # 0| 1|2 etc(tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range (3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for(i,spot) in enumerate(self.board):
        #     # ['x', 'x', 'o' ] --> ()
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square]= letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self,square,letter):
        # winner if 3 in a row anywhere.. we have to check anywhere!
        row_ind = square // 3
        row = self.board[row_ind *3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # check column
        col_ind = square  % 3
        column = [self.board[col_ind+ i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True           
        
def play(game, x_player , o_player, print_game= True):
    
    if print_game:
        game.print_board_nums()
        
    letter = 'X' # starting letter
    
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        #let's define a function to make a move!
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #just empty line
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
        # tiny break
        if print_game:
            time.sleep(0.8)    
    if print_game:
        print('It\'s a tie')
        
        
                
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    result = play(t,x_player,o_player, print_game= True)
    # x_wins = 0
    # o_wins = 0
    # ties = 0
    # for _ in range(1000):            
    #     x_player = RandomComputerPlayer('X')
    #     o_player = GeniusComputerPlayer('O')
    #     t = TicTacToe()
    #     result = play(t,x_player,o_player, print_game= False)
    #     if result == 'X':
    #         x_wins += 1
    #     elif result =='O':
    #         o_wins +=1
    #     else:
    #         ties +=1
    # print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins and {ties} Tie')