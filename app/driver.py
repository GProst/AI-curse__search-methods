import time

from params import search_type
from output_manager import output_result, search_time
from path import Path
from bfs_search import bfs_search
from dfs_search import dfs_search
from ast_search import ast_search

# choosing search type abd executing search
search_time['start'] = time.time()

search = {
    'bfs': bfs_search,
    'dfs': dfs_search,
    'ast': ast_search
}.get(search_type)()

# creating a path to goal
Path.create_path()
search_time['end'] = time.time()

# outputting result of the search
output_result()
