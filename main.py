import time
from agent import *
from board import *

def main(file_name, max_time, reward, success_prob, timebased):
    init = time.time()
    read_board(file_name)
    while (time.time() - init < max_time):
        pass