import time
import sys
import agent
import gridWorld
import csv
import board

def main():
    #board_file = sys.argv[1]
    board_file = "test0.txt"
    
    #run_time = sys.argv[2]
    #action_penalty = sys.argv[3]
    #transition_model = sys.argv[4]
    #time_based = sys.argv[5]
    #run(board_file, float(run_time), action_penalty, transition_model, time_based)
    
    grid_environment = board.Board(board_file)
    
    ag = gridWorld.Agent(grid_environment)
    ag.play(1)
    print(ag.showValues()) 

if __name__ == "__main__":
    main()