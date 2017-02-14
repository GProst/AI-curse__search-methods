from params import goal_state, n, state_length, search_type

visited_nodes_states_collection = set()


class _NodesExpanded(object):
    list = []
    length = 0

    def append(self, node):
        self.list.append(node)
        self.length += 1


nodes_expanded = _NodesExpanded()


def remove_redundant_nodes_from_expanded_nodes_list(parent_node_index):  # dfs/dls only
    del nodes_expanded.list[parent_node_index + 1:]


class _Node:
    def __init__(self):
        self.state = None
        self.parent_index_in_list_of_expanded_nodes = None
        self.move = None
        self.position_of_0_in_state = None
        self.depth_level = None


# class, that represents current node in queue/stack
# class is also represents the goal node after the search is over
class _CurrentNode(_Node):
    def __init__(self):
        _Node.__init__(self)

    def is_goal_node(self):
        return self.state == goal_state

    def add_to_expanded(self):
        """
        Node format in the list of extended nodes is a tuple, which equals to:
        (parent_index_in_list_of_expanded_nodes, move).
        `move` is a move which leaded to this node from its parent.
        `move` is an integer with possible values of 0,1,2,3
        which corresponds to 'Up', 'Down', 'Left', 'Right'.
        Initial node will have -1 for both `parent_index_in_list_of_expanded_nodes` and `move`
        because initial node doesn't have a parent and there were was no allowed moves
        on added it to the list
        """
        nodes_expanded.append((self.parent_index_in_list_of_expanded_nodes, self.move))

    def update(self, node):
        self.state = node[0]
        self.parent_index_in_list_of_expanded_nodes = node[1]
        self.move = node[2]
        self.depth_level = node[3]
        self.position_of_0_in_state = current_node.state.index(0)

    def has_top_successor(self):
        return (self.position_of_0_in_state - n) > -1

    def has_bottom_successor(self):
        return (self.position_of_0_in_state + n) < state_length

    def has_left_successor(self):
        return (self.position_of_0_in_state % n) != 0

    def has_right_successor(self):
        return ((self.position_of_0_in_state + 1) % n) != 0


# class represents successor of current node in a queue/stack
class _SuccessorNode(_Node):
    def __init__(self):
        _Node.__init__(self)
        """
        We know that parent of the first level successor nodes will have index of 0
        in the list of extended nodes
        """
        self.parent_index_in_list_of_expanded_nodes = 0

    def transform_into_top_successor(self):
        self._create_common_properties()
        self.position_of_0_in_state = current_node.position_of_0_in_state - n
        number_to_switch = current_node.state[self.position_of_0_in_state]
        self.state = current_node.state[:self.position_of_0_in_state] \
                     + (0,) \
                     + current_node.state[
                       self.position_of_0_in_state
                       + 1:current_node.position_of_0_in_state] \
                     + (number_to_switch,) \
                     + current_node.state[current_node.position_of_0_in_state + 1:]
        self.move = 0

    def transform_into_bottom_successor(self):
        self._create_common_properties()
        self.position_of_0_in_state = current_node.position_of_0_in_state + n
        number_to_switch = current_node.state[self.position_of_0_in_state]
        self.state = current_node.state[:current_node.position_of_0_in_state] \
                     + (number_to_switch,) \
                     + current_node.state[
                       current_node.position_of_0_in_state
                       + 1:self.position_of_0_in_state
                       ] \
                     + (0,) \
                     + current_node.state[self.position_of_0_in_state + 1:]
        self.move = 1

    def transform_into_left_successor(self):
        self._create_common_properties()
        self.position_of_0_in_state = current_node.position_of_0_in_state - 1
        number_to_switch = current_node.state[self.position_of_0_in_state]
        self.state = current_node.state[:self.position_of_0_in_state] \
                     + (0, number_to_switch,) \
                     + current_node.state[current_node.position_of_0_in_state + 1:]
        self.move = 2

    def transform_into_right_successor(self):
        self._create_common_properties()
        self.position_of_0_in_state = current_node.position_of_0_in_state + 1
        number_to_switch = current_node.state[self.position_of_0_in_state]
        self.state = current_node.state[:current_node.position_of_0_in_state] \
                     + (number_to_switch, 0,) \
                     + current_node.state[self.position_of_0_in_state + 1:]
        self.move = 3

    def _create_common_properties(self):
        self.depth_level = current_node.depth_level + 1
        """
        Parent of next successor nodes will be the last one which we added
        to the list of extended nodes. That's why we can increase index
        of next successor nodes by 1 beforehand.
        """
        self.parent_index_in_list_of_expanded_nodes = nodes_expanded.length


class _DFSSuccessorNode(_SuccessorNode):
    def __init__(self):
        _SuccessorNode.__init__(self)

    def _create_common_properties(self):
        self.depth_level = current_node.depth_level + 1
        self.parent_index_in_list_of_expanded_nodes = \
            current_node.parent_index_in_list_of_expanded_nodes + 1


class _DFSCurrentNode(_CurrentNode):
    def __init__(self):
        _CurrentNode.__init__(self)
        self.is_a_leaf = False


class _ASTNode:
    def __init__(self):
        self.value = None


class _ASTCurrentNode(_ASTNode, _CurrentNode):
    def __init__(self):
        _ASTNode.__init__(self)
        _CurrentNode.__init__(self)


class _ASTSuccessorNode(_ASTNode, _SuccessorNode):
    def __init__(self):
        _ASTNode.__init__(self)
        _SuccessorNode.__init__(self)

    def count_manhattan_value(self):
        _count_manhattan_value(self)


class _IDASuccessorNode(_ASTNode, _DFSSuccessorNode):
    def __init__(self):
        _ASTNode.__init__(self)
        _DFSSuccessorNode.__init__(self)

    def count_manhattan_value(self):
        _count_manhattan_value(self)


def _count_manhattan_value(node):
    state = node.state
    value = 0
    for i in range(0, n - 1):
        value += state.index(i) - i
    node.value = node.depth_level + value  # g(n) + h(n)


current_node = {
    'bfs': _CurrentNode,
    'dfs': _DFSCurrentNode,
    'ast': _ASTCurrentNode,
    'ida': _DFSCurrentNode
}.get(search_type)()

successor_node = {
    'bfs': _SuccessorNode,
    'dfs': _DFSSuccessorNode,
    'ast': _ASTSuccessorNode,
    'ida': _IDASuccessorNode
}.get(search_type)()
