import numpy as np
import state
import time

class Agent:

    def __init__(self, grid_environment, lr=0.2,exp_rate =0.2):
        self.states = []
        self.actions = ["up", "down", "left", "right"]
        
        self.lr = lr
        self.exp_rate = exp_rate
        self.grid_environment = grid_environment
        
        # Create state using the board and the start position
        self.State = state.State(self.grid_environment,self.grid_environment.start)

        # initial state reward
        self.state_values = {}
        for i in range(len(self.grid_environment.board)):
            for j in range(len(self.grid_environment.board[0])):
                self.state_values[(i, j)] = 0  # set initial value to 0

    def chooseAction(self):
        # choose action with most expected value
        mx_nxt_reward = 0
        action = ""

        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy action
            for a in self.actions:
                nxt_reward = self.state_values[self.State.nxtPosition(a)]
                if nxt_reward >= mx_nxt_reward:
                    action = a
                    mx_nxt_reward = nxt_reward
        return action

    def takeAction(self, action):
        position = self.State.nxtPosition(action)
        return state.State(self.grid_environment, state=position)

    def reset(self):
        self.states = []
        self.State = state.State(self.grid_environment,self.grid_environment.start)

    def play(self, max_time=1):
        init = time.time()
        while (time.time() - init < max_time):
            
            # to the end of game back propagate reward
            if self.State.isEnd:
                # back propagate
                reward = self.State.giveReward()
                # explicitly assign end state to reward values
                self.state_values[self.State.state] = reward  # this is optional
                #print("Game End Reward", reward)
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.lr * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                self.reset()
            else:
                action = self.chooseAction()
                # append trace
                self.states.append(self.State.nxtPosition(action))
                #print("current position {} action {}".format(self.State.state, action))
                # by taking the action, it reaches the next state
                self.State = self.takeAction(action)
                # mark is end
                self.State.isEndFunc()
                #print("nxt state", self.State.state)
                #print("---------------------")

    def showValues(self):
        for i in range(0, len(self.grid_environment.board)):
            print('----------------------------------')
            out = '| '
            for j in range(0, len(self.grid_environment.board[0])):
                out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('----------------------------------')