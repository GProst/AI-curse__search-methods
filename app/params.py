import sys
import math

search_type = sys.argv[1]
init_state = tuple(map(int, (sys.argv[2].split(','))))  # to tuple of integers
goal_state = tuple(sorted(init_state))
n = int(math.sqrt(len(init_state)))  # width/hight of the table
state_length = n * n
