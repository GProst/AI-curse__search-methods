from nodes import nodes_expanded, current_node as goal_node


class Path:
    path_to_goal = []
    __move_map = {
        0: 'Up',
        1: 'Down',
        2: 'Left',
        3: 'Right'
    }

    @classmethod
    def create_path(cls):
        expanded = nodes_expanded.list
        # we are searching though the list of expanded nodes, which are tuples with the next format:
        # (parent_index_in_list_of_expanded_nodes, move)
        (parent_index, move_code) = goal_node.parent_index_in_list_of_expanded_nodes, goal_node.move
        while parent_index > -1:
            cls.path_to_goal.insert(0, cls.__move_map.get(move_code))
            (parent_index, move_code) = expanded[parent_index]
