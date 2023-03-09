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

    def isLegal(self, state):
        if (state[0] >= 0) and (state[0] <= (len(self.grid_environment.board) - 1)):
            if (state[1] >= 0) and (state[1] <= (len(self.grid_environment.board[0]) - 1)):
                if state not in self.grid_environment.barriers:
                    return True
        return False

    def movement(self, action):
        if action == "up":
            nxtState = (self.state[0] - 1, self.state[1])
        elif action == "down":
            nxtState = (self.state[0] + 1, self.state[1])
        elif action == "left":
            nxtState = (self.state[0], self.state[1] - 1)
        elif action == "right":
            nxtState = (self.state[0], self.state[1] + 1)
        return nxtState

    def jump(self, action):
        # two steps
        if action == "up up":
            nxtState = (self.state[0] - 2, self.state[1])
        elif action == "down down":
            nxtState = (self.state[0] + 2, self.state[1])
        elif action == "left left":
            nxtState = (self.state[0], self.state[1] - 2)
        elif action == "right right":
            nxtState = (self.state[0], self.state[1] + 2)

        return nxtState

    def nxtPosition(self, action):
        action = self.transitionModel(action)
        # action = "down down"

        if len(action.split()) == 2:
            nxtState = self.jump(action)
            # if next state legal
            if self.isLegal(nxtState):
                return nxtState
            else:
                nxtState = self.movement(action.split()[0])
                if self.isLegal(nxtState):
                    return nxtState
                else:
                    return self.state
        else:
            nxtState = self.movement(action)
            if self.isLegal(nxtState):
                return nxtState
            else:
                return self.state
