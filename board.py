import csv

class Board:
    def __init__(self, filename):    
        self.board = self.read(filename)
        self.start = [(ind, self.board[ind].index('S')) for ind in range(len(self.board)) if 'S' in self.board[ind]][0]
        self.win_states = self.find_win_states()
        self.lose_states = self.find_lose_states()
        self.barriers = [(ind, self.board[ind].index('X')) for ind in range(len(self.board)) if 'X' in self.board[ind]]
        self.cookies = [(ind, self.board[ind].index('+')) for ind in range(len(self.board)) if '+' in self.board[ind]]
        self.glass = [(ind, self.board[ind].index('-')) for ind in range(len(self.board)) if '-' in self.board[ind]]

    def read(self, board_file):
        board_array = []
        with open(board_file,newline = '') as board:
            board_data = csv.reader(board, delimiter='\t')
            for row in board_data:
                board_array.append(row)
        return board_array

    def find_win_states(self):
        win_states = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if float(self.board[i][j]) > 0:
                        win_states.append((i,j))
                except ValueError:
                    continue
        return win_states
    
    def find_lose_states(self):
        lose_states = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if float(self.board[i][j]) < 0:
                        lose_states.append((i,j))
                except ValueError:
                    continue
        return lose_states