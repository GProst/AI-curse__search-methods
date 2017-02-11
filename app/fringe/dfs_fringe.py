from .fringe import Fringe
from params import init_state
from nodes import successor_node, current_node, remove_redundant_nodes_from_expanded_nodes_list


class _DFSFringe(Fringe):
    def __init__(self):
        Fringe.__init__(self)
        """
        Node format is a tuple, which equals to:
        (node_state, parent_index_in_list_of_expanded_nodes, move, depth_level).
        `move` is a move which leaded to this node from its parent.
        `move` is an integer with possible values of 0,1,2,3
        which corresponds to 'Up', 'Down', 'Left', 'Right'.
        Initial node will have -1 for both `parent_index_in_list_of_expanded_nodes` and `move`
        because initial node doesn't have a parent and there were was no allowed moves
        on added it to the list
        """
        self._fringe.append((init_state, -1, -1, 0))

    def push(self):
        self._common_actions_before_adding_new_node()
        self._fringe.insert(0, (successor_node.state,
                                successor_node.parent_index_in_list_of_expanded_nodes,
                                successor_node.move, successor_node.depth_level))

    def pop(self):
        next_node = self._fringe.pop(0)
        self._common_actions_after_removing_node(next_node[0])
        if current_node.is_a_leaf:
            remove_redundant_nodes_from_expanded_nodes_list(next_node[1])
        # when we remove node from fringe, we actually make it current node in search
        current_node.update(next_node)


dfs_fringe = _DFSFringe()
