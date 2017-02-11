from nodes import current_node, successor_node
from states_collections import states_collection, fringe_states_collection
from fringe.ast_fringe import ast_fringe


def ast_search():
    while ast_fringe.size > 0:
        ast_fringe.delete_min()
        if current_node.is_goal_node():
            return True
        else:
            __expand_node()


def __expand_node():
    __try_add_upper_node_to_fringe()
    __try_add_lower_node_to_fringe()
    __try_add_left_node_to_fringe()
    __try_add_right_node_to_fringe()
    current_node.add_to_expanded()


def __try_add_upper_node_to_fringe():
    if current_node.has_top_successor():
        successor_node.transform_into_top_successor()
        if __not_visited() or __not_duplicate_with_higher_value():
            ast_fringe.enqueue()


def __try_add_lower_node_to_fringe():
    if current_node.has_bottom_successor():
        successor_node.transform_into_bottom_successor()
        if __not_visited() or __not_duplicate_with_higher_value():
            ast_fringe.enqueue()


def __try_add_left_node_to_fringe():
    if current_node.has_left_successor():
        successor_node.transform_into_left_successor()
        if __not_visited() or __not_duplicate_with_higher_value():
            ast_fringe.enqueue()


def __try_add_right_node_to_fringe():
    if current_node.has_right_successor():
        successor_node.transform_into_right_successor()
        if __not_visited() or __not_duplicate_with_higher_value():
            ast_fringe.enqueue()


def __not_visited():
    if successor_node.state not in states_collection:
        successor_node.count_manhattan_value()
        return True


def __not_duplicate_with_higher_value():
    if successor_node.state in fringe_states_collection:
        duplicate_node_index, duplicate_node = ast_fringe.find_duplicate()
        """
        we are comparing only depth_level(g(n)), because we know that h(n) of duplicate nodes are
        equal
        """
        if successor_node.depth_level < duplicate_node.depth_level:
            ast_fringe.remove_duplicate_node(duplicate_node_index)
            return True
        else:
            return False
    else:
        return False