import resource
from path import Path
from params import search_type
from fringe.bfs_fringe import bfs_fringe
from fringe.dfs_fringe import dfs_fringe
from fringe.ast_fringe import ast_fringe
from fringe.ida_fringe import ida_fringe
from nodes import nodes_expanded, current_node as goal_node

search_time = {
    'start': None,
    'end': None
}

fringe = {
    'bfs': bfs_fringe,
    'dfs': dfs_fringe,
    'ast': ast_fringe,
    'ida': ida_fringe
}.get(search_type)


def output_result():
    output = {
        'path_to_goal': Path.path_to_goal,
        'cost_of_path': goal_node.depth_level,
        'nodes_expanded': nodes_expanded.length,
        'fringe_size': fringe.size,
        'max_fringe_size': fringe.max_size,
        'max_search_depth': fringe.max_search_depth,
        'running_time': search_time['end'] - search_time['start'],
        'max_ram_usage': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    }
    # TODO: reformat the path:
    output_file = open('./app/output.txt', 'w')
    output_string = ("path_to_goal: {path_to_goal}\n"
                     "cost_of_path: {cost_of_path}\n"
                     "nodes_expanded: {nodes_expanded}\n"
                     "fringe_size: {fringe_size}\n"
                     "max_fringe_size: {max_fringe_size}\n"
                     "search_depth: {cost_of_path}\n"
                     "max_search_depth: {max_search_depth}\n"
                     "running_time: {running_time:.8f}\n"
                     "max_ram_usage: {max_ram_usage:.8f}\n"
                     ).format(**output)
    output_file.write(output_string)
