import time

from output_manager import output_result, search_time
from params import search_type
from path import Path
from search_methods.bfs_search import bfs_search
from search_methods.dfs_search import dfs_search
from search_methods.ast_search import ast_search
from search_methods.ida_search import ida_search

# choosing search type abd executing search
search_time['start'] = time.time()

search = {
    'bfs': bfs_search,
    'dfs': dfs_search,
    'ast': ast_search,
    'ida': ida_search
}.get(search_type)()

# creating a path to goal
Path.create_path()
search_time['end'] = time.time()

# outputting result of the search
output_result()
