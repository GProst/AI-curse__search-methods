from nodes import current_node, successor_node, visited_nodes_states_collection
from fringe.ast_fringe import ast_fringe


def ast_search():
    while ast_fringe.size > 0:
        ast_fringe.delete_min()
        if current_node.is_goal_node():
            return True
        else:
            __expand_node()
    return False


def __expand_node():
    __try_add_upper_node_to_fringe()
    __try_add_lower_node_to_fringe()
    __try_add_left_node_to_fringe()
    __try_add_right_node_to_fringe()
    current_node.add_to_expanded()


def __try_add_upper_node_to_fringe():
    if current_node.has_top_successor():
        successor_node.transform_into_top_successor()
        if (__not_in_fringe_and_not_visited()) or __in_fringe_with_bigger_value():
            ast_fringe.enqueue()


def __try_add_lower_node_to_fringe():
    if current_node.has_bottom_successor():
        successor_node.transform_into_bottom_successor()
        if (__not_in_fringe_and_not_visited()) or __in_fringe_with_bigger_value():
            ast_fringe.enqueue()


def __try_add_left_node_to_fringe():
    if current_node.has_left_successor():
        successor_node.transform_into_left_successor()
        if (__not_in_fringe_and_not_visited()) or __in_fringe_with_bigger_value():
            ast_fringe.enqueue()


def __try_add_right_node_to_fringe():
    if current_node.has_right_successor():
        successor_node.transform_into_right_successor()
        if (__not_in_fringe_and_not_visited()) or __in_fringe_with_bigger_value():
            ast_fringe.enqueue()


def __not_in_fringe_and_not_visited():
    if successor_node.state not in ast_fringe.states_collection and \
                    successor_node.state not in visited_nodes_states_collection:
        successor_node.count_manhattan_value()
        return True
    else:
        return False


def __in_fringe_with_bigger_value():  # if node is already in the fringe, but with bigger value
    if __in_fringe():
        duplicate_node_index, duplicate_node_depth_level, \
        duplicate_node_value = ast_fringe.find_duplicate()
        """
        we are comparing only depth_level(g(n)), because we know that h(n) of duplicate nodes are
        equal
        """
        if successor_node.depth_level < duplicate_node_depth_level:
            successor_node.value = duplicate_node_value - duplicate_node_depth_level \
                                   + successor_node.depth_level
            ast_fringe.remove_duplicate_node(duplicate_node_index)
            return True
        else:
            return False
    else:
        return False


def __in_fringe():
    return successor_node.state in ast_fringe.states_collection
