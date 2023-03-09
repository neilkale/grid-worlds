import numpy as np
# import board
# import agent


class State:
    def __init__(self, grid_environment, state):
        self.grid_environment = grid_environment
        self.state = state
        self.isEnd = False

    def giveReward(self):
        # print(self.state, self.grid_environment.cookies, self.visited_cookies)
        if self.state in self.grid_environment.terminal_states:
            return float(self.grid_environment.board[self.state[0]][self.state[1]])
        else:
            return 0

    def isEndFunc(self):
        if self.state in self.grid_environment.terminal_states:
            self.isEnd = True

    def transitionModel(self, action):
        p_success = 0.7
        p_jump = 0.15
        p_backward = 0.15

        if action == "up":
            return np.random.choice(["up", "down", "up up"], p=[p_success, p_backward, p_jump])
        if action == "down":
            return np.random.choice(["down", "up", "down down"], p=[p_success, p_backward, p_jump])
        if action == "left":
            return np.random.choice(["left", "right", "left left"], p=[p_success, p_backward, p_jump])
        if action == "right":
            return np.random.choice(["right", "left", "right right"], p=[p_success, p_backward, p_jump])

    def movement(self, action):
        if action == "up":
            nxtState = (self.state[0] - 1, self.state[1])
        elif action == "down":
            nxtState = (self.state[0] + 1, self.state[1])
        elif action == "left":
            nxtState = (self.state[0], self.state[1] - 1)
        else:
            nxtState = (self.state[0], self.state[1] + 1)
            
        return nxtState

    def nxtPosition(self, action):
        action = self.transitionModel(action)
        action = action.split()

        for a in action:
            nxtState = self.movement(a) 

            # if next state legal
            if (nxtState[0] >= 0) and (nxtState[0] <= (len(self.grid_environment.board) -1)):
                if (nxtState[1] >= 0) and (nxtState[1] <= (len(self.grid_environment.board[0]) -1)):
                    if nxtState not in self.grid_environment.barriers:
                        return nxtState
            #  if next state illegal stay at same state
            return self.state
