import numpy as np
import board
import gridWorld
# global variables

class State:
    def __init__(self, grid_environment, state):
        self.grid_environment = grid_environment
        self.state = state
        self.isEnd = False
        
    def giveReward(self):
        #print(self.state, self.grid_environment.cookies, self.visited_cookies)
        if self.state in self.grid_environment.terminal_states:
            return float(self.grid_environment.board[self.state[0]][self.state[1]])
        else:
            return 0

    def isEndFunc(self):
        if self.state in self.grid_environment.terminal_states:
            self.isEnd = True

    def nxtPosition(self, action):    
        if action == "up":
            nxtState = (self.state[0] - 1, self.state[1])
        elif action == "down":
            nxtState = (self.state[0] + 1, self.state[1])
        elif action == "left":
            nxtState = (self.state[0], self.state[1] - 1)
        else:
            nxtState = (self.state[0], self.state[1] + 1)
        
        # if next state legal
        if (nxtState[0] >= 0) and (nxtState[0] <= (len(self.grid_environment.board) -1)):
            if (nxtState[1] >= 0) and (nxtState[1] <= (len(self.grid_environment.board[0]) -1)):
                if nxtState not in self.grid_environment.barriers:
                    return nxtState
        return self.state
