from enum import Enum
from board import *

ACTION_SET = Enum('ACTION_SET', ['LEFT','RIGHT','UP','DOWN'])
Q = [[[]]]
state = [0,0]

def take_action(s,a):
    pass

def calculate_policy(s):
    U_e = []
    for action in ACTION_SET:
        next_state = next_state(s, action)
        
    return s2    

# def movement(direction):
#     pass

# def utilityFunction():
#     pass

# def transitionModel():
#     pass

# def printResult():
#     pass

def print_policy():
    pass