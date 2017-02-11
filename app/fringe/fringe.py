from nodes import successor_node, visited_nodes_states_collection
from params import init_state


class Fringe:
    def __init__(self):
        self._fringe = []
        self.states_collection = set([init_state])  # adding initial state to our states collection
        self._max_search_depth = 0
        self.size = 1  # we already have 1 initial node in fringe at the beginning
        self._max_size = 1

    def _increase_size_and_check_max(self):
        self.size += 1
        if self.size > self._max_size:
            self._max_size = self.size

    def _check_max_depth(self):
        successor_node_depth = successor_node.depth_level
        if self._max_search_depth < successor_node_depth:
            self._max_search_depth = successor_node_depth

    @property
    def max_search_depth(self):
        return self._max_search_depth

    @property
    def max_size(self):
        return self._max_size

    def _common_actions_before_adding_new_node(self):
        self._check_max_depth()
        self._increase_size_and_check_max()
        self.states_collection.add(successor_node.state)

    def _common_actions_after_removing_node(self, next_state):
        self.size -= 1
        visited_nodes_states_collection.add(next_state)
        self.states_collection.remove(next_state)
