import numpy as np
import state
import time

class Agent:

    def __init__(self, grid_environment, lr=0.2, exp_rate=0.2, action_penalty=0):
        self.states = []
        self.actions = ["up", "down", "left", "right"]

        self.lr = lr
        self.exp_rate = exp_rate
        self.grid_environment = grid_environment
        self.grid_size = self.get_size(self.grid_environment.board)
        self.action_penalty = action_penalty

        # Create state using the board and the start position
        self.State = state.State(
            self.grid_environment, self.grid_environment.start)

        # initial state reward
        self.state_values = {}
        for i in range(len(self.grid_environment.board)):
            for j in range(len(self.grid_environment.board[0])):
                self.state_values[(i, j)] = 0  # set initial value to 0
        self.heat_map = {}
        for i in range(len(self.grid_environment.board)):
            for j in range(len(self.grid_environment.board[0])):
                self.heat_map[(i, j)] = 0  # set initial value to 0
        self.visited_cookies = []
        self.visited_glass = []

    def get_size(self, board):
        return [len(board), len(board[0])]

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
        action = self.transitionModel(action)
        position = self.State.nxtPosition(action)
        return state.State(self.grid_environment, state=position)

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

    def reset(self):
        self.states = []
        self.State = state.State(
            self.grid_environment, self.grid_environment.start)
        self.visited_cookies = []
        self.visited_glass = []

    def play(self, max_time=1):
        init = time.time()
        while (time.time() - init < max_time):

            # to the end of game back propagate reward
            if self.State.isEnd:
                # back propagate
                reward = self.State.giveReward()
                # explicitly assign end state to reward values
                # this is optional
                self.state_values[self.State.state] = reward
                #print("Game End Reward", reward)
                action_counter = 1
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.lr * (
                        reward - self.state_values[s] + action_counter*self.action_penalty)
                    self.state_values[s] = round(reward, 3)
                    self.heat_map[s] = self.heat_map[s] + 1
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
                # print("---------------------")

    def showValues(self):
        for i in range(0, len(self.grid_environment.board)):
            print('-'*(9*len(self.grid_environment.board[0])+1))
            out = '| '
            for j in range(0, len(self.grid_environment.board[0])):
                val = (i, j)
                if val in self.grid_environment.barriers:
                    out += 'X'.ljust(6) + ' | '
                elif val in self.grid_environment.win_states or val in self.grid_environment.lose_states:
                    out += str(self.grid_environment.board[i]
                               [j]).ljust(6) + ' | '
                else:
                    out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('-'*(9*len(self.grid_environment.board[0])+1))

    def showHeatMap(self):
        total = 0
        for i in range(len(self.grid_environment.board)):
            for j in range(len(self.grid_environment.board[0])):
                total += self.heat_map[(i, j)]

        for i in range(0, len(self.grid_environment.board)):
            print('-'*(9*len(self.grid_environment.board[0])+1))
            out = '| '
            for j in range(0, len(self.grid_environment.board[0])):
                val = (i, j)
                if val in self.grid_environment.barriers:
                    out += 'X'.ljust(6) + ' | '
                elif val in self.grid_environment.win_states or val in self.grid_environment.lose_states:
                    out += str(self.grid_environment.board[i]
                               [j]).ljust(6) + ' | '
                else:
                    out += str(round(100 *
                               self.heat_map[(i, j)]/total, 2)).ljust(6) + ' | '
            print(out)
        print('-'*(9*len(self.grid_environment.board[0])+1))

    def showPolicy(self):
        for i in range(0, len(self.grid_environment.board)):
            print('-'*(9*len(self.grid_environment.board[0])+1))
            out = '| '
            for j in range(0, len(self.grid_environment.board[0])):
                mx_nxt_reward = -10
                val = (i, j)
                it_state = state.State(self.grid_environment, val)
                if val in self.grid_environment.barriers:
                    token = 'X'
                elif val in self.grid_environment.win_states or val in self.grid_environment.lose_states:
                    token = str(self.grid_environment.board[i][j])
                else:
                    action = 'up'
                    for a in self.actions:
                        nxt_reward = self.state_values[it_state.nxtPosition(a)]
                        if nxt_reward >= mx_nxt_reward:
                            #print(a, nxt_reward, mx_nxt_reward)
                            action = a
                            mx_nxt_reward = nxt_reward
                        token = self.get_token(action)
                out += token.ljust(6) + ' | '
            print(out)
        print('-'*(9*len(self.grid_environment.board[0])+1))

    def get_token(self, action):
        if action == "up":
            token = "^"
        if action == "down":
            token = "V"
        if action == "right":
            token = ">"
        if action == "left":
            token = "<"
        return token
