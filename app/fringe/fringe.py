from states_collections import states_collection
from nodes import successor_node


class Fringe:
    def __init__(self):
        self._fringe = []
        self._max_search_depth = 0
        self._size = 1  # we already have 1 initial node in fringe at the beginning
        self._max_size = 1

    def _increase_size_and_check_max(self):
        self._size += 1
        if self._size > self._max_size:
            self._max_size = self._size

    def _check_max_depth(self):
        successor_node_depth = successor_node.depth_level
        if self._max_search_depth < successor_node_depth:
            self._max_search_depth = successor_node_depth

    @property
    def max_search_depth(self):
        return self._max_search_depth

    @property
    def size(self):
        return self._size

    @property
    def max_size(self):
        return self._max_size

    def _common_actions_before_adding_new_node(self):
        self._check_max_depth()
        self._increase_size_and_check_max()
        states_collection.add(successor_node.state)
