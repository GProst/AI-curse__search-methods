from fringe.dfs_fringe import dfs_fringe
from nodes import current_node, successor_node
from states_collections import states_collection


def dfs_search():
    while dfs_fringe.size > 0:
        dfs_fringe.pop()
        if current_node.is_goal_node():
            return True
        else:
            __expand_node()


def __expand_node():
    __try_add_right_node_to_fringe()
    __try_add_left_node_to_fringe()
    __try_add_lower_node_to_fringe()
    __try_add_upper_node_to_fringe()
    current_node.add_to_expanded()


def __try_add_upper_node_to_fringe():
    if current_node.has_top_successor():
        successor_node.transform_into_top_successor()
        if successor_node.state not in states_collection:
            dfs_fringe.push()


def __try_add_lower_node_to_fringe():
    if current_node.has_bottom_successor():
        successor_node.transform_into_bottom_successor()
        if successor_node.state not in states_collection:
            dfs_fringe.push()


def __try_add_left_node_to_fringe():
    if current_node.has_left_successor():
        successor_node.transform_into_left_successor()
        if successor_node.state not in states_collection:
            dfs_fringe.push()


def __try_add_right_node_to_fringe():
    if current_node.has_right_successor():
        successor_node.transform_into_right_successor()
        if successor_node.state not in states_collection:
            dfs_fringe.push()
