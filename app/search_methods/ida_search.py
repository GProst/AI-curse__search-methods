from fringe.ida_fringe import ida_fringe
from nodes import current_node, successor_node, visited_nodes_states_collection, nodes_expanded

bound = 0


def ida_search():
    global bound
    while True:
        if dls_plus_a_star_search():
            return True
        else:
            bound += 1
            __reinitialize_dls_search()


def __reinitialize_dls_search():
    ida_fringe.reinitialize()
    visited_nodes_states_collection.clear()
    del nodes_expanded.list[:]
    nodes_expanded.length = 0


def dls_plus_a_star_search():
    while ida_fringe.size > 0:
        ida_fringe.pop()
        if current_node.is_goal_node():
            return True
        else:
            __expand_node()
    return False


def __expand_node():
    current_node.is_a_leaf = __try_add_right_node_to_fringe() & \
                             __try_add_left_node_to_fringe() & \
                             __try_add_lower_node_to_fringe() & \
                             __try_add_upper_node_to_fringe()
    current_node.add_to_expanded()


def __try_add_upper_node_to_fringe():
    if current_node.has_top_successor():
        successor_node.transform_into_top_successor()
        if successor_node.state not in ida_fringe.states_collection and \
                        successor_node.state not in visited_nodes_states_collection:
            successor_node.count_manhattan_value()
            if successor_node.value > bound:
                return True
            else:
                ida_fringe.push()
                return False
    return True


def __try_add_lower_node_to_fringe():
    if current_node.has_bottom_successor():
        successor_node.transform_into_bottom_successor()
        if successor_node.state not in ida_fringe.states_collection and \
                        successor_node.state not in visited_nodes_states_collection:
            successor_node.count_manhattan_value()
            if successor_node.value > bound:
                return True
            else:
                ida_fringe.push()
                return False
    return True


def __try_add_left_node_to_fringe():
    if current_node.has_left_successor():
        successor_node.transform_into_left_successor()
        if successor_node.state not in ida_fringe.states_collection and \
                        successor_node.state not in visited_nodes_states_collection:
            successor_node.count_manhattan_value()
            if successor_node.value > bound:
                return True
            else:
                ida_fringe.push()
                return False
    return True


def __try_add_right_node_to_fringe():
    if current_node.has_right_successor():
        successor_node.transform_into_right_successor()
        if successor_node.state not in ida_fringe.states_collection and \
                        successor_node.state not in visited_nodes_states_collection:
            successor_node.count_manhattan_value()
            if successor_node.value > bound:
                return True
            else:
                ida_fringe.push()
                return False
    return True
