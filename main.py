import time
import sys
import agent
import gridWorld
import csv
import board

def run(file_name, max_time, action_penalty, transition_model, time_based):
    init = time.time()
    #while (time.time() - init < max_time):
    agent.play(10,file_name)

#def read(board_file):
#    board_array = []
#    with open(board_file,newline = '') as board:
#        board_data = csv.reader(board, delimiter='\t')
#        for row in board_data:
#            board_array.append(row)
#    return board_array

def main():
    #board_file = sys.argv[1]
    board_file = "test0.txt"
    
    #run_time = sys.argv[2]
    #action_penalty = sys.argv[3]
    #transition_model = sys.argv[4]
    #time_based = sys.argv[5]
    #run(board_file, float(run_time), action_penalty, transition_model, time_based)
    
    grid_environment = board.Board(board_file)
    #print(([(ind, board[ind].index('1')) for ind in range(len(board)) if '1' in board[ind]][0]))
    
    ag = gridWorld.Agent(grid_environment)
    ag.play(10)
    print(ag.showValues()) 

if __name__ == "__main__":
    main()