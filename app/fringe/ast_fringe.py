from .fringe import Fringe
from params import init_state
from states_collections import states_collection
from nodes import successor_node, current_node


class _ASTFringe(Fringe):
    def __init__(self):
        Fringe.__init__(self)
        """
        Node format is a tuple, which equals to:
        (node_state, parent_index_in_list_of_expanded_nodes, move, depth_level, value).
        `move` is a move which leaded to this node from its parent.
        `move` is an integer with possible values of 0,1,2,3
        which corresponds to 'Up', 'Down', 'Left', 'Right'.
        Initial node will have -1 for both `parent_index_in_list_of_expanded_nodes` and `move`
        because initial node doesn't have a parent and there were was no allowed moves
        on added it to the list
        `depth_level` is actually g(n)
        `value` is h(n), Manhattan priority function value of `state`. For initial node it is
        equal to None, because it doesn't matter as we are gonna mark this node as expanded
        in a moment.
        """
        self._fringe.append((init_state, -1, -1, 0, None))
        states_collection.add(init_state)  # adding initial state to our states collection

    def enqueue(self):
        self._common_actions_before_adding_new_node()
        self._fringe.append((successor_node.state,
                             successor_node.parent_index_in_list_of_expanded_nodes,
                             successor_node.move, successor_node.depth_level, successor_node.value))

    def delete_min(self):
        self._size -= 1
        # when we remove node from fringe, we actually make it current node in search
        current_node_index = self._fringe.index(min(self._fringe, key=lambda node: node[4]))
        current_node.update(self._fringe.pop(current_node_index))

    def find_duplicate(self):
        state_to_search = successor_node.state
        for index, node in self._fringe:
            if node.state == state_to_search:
                return index, node

    def remove_duplicate_node(self, duplicate_node_index):
        self._fringe.pop(duplicate_node_index)


ast_fringe = _ASTFringe()
