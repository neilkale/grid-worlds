import time
import sys
import agent
import csv
import board

def main():
    #board_file = sys.argv[1]
    board_file = "test1.txt"
    
    #run_time = sys.argv[2]
    #action_penalty = sys.argv[3]
    action_penalty = -0.1
    #transition_model = sys.argv[4]
    #time_based = sys.argv[5]
    #run(board_file, float(run_time), action_penalty, transition_model, time_based)
    
    grid_environment = board.Board(board_file)
    
    ag = agent.Agent(grid_environment,action_penalty=action_penalty)
    ag.play(10)
    print('Utility Values')
    ag.showValues()
    print('Agent Time Spent Heat Map')
    ag.showHeatMap()
    print('Policy')
    ag.showPolicy()

if __name__ == "__main__":
    main()