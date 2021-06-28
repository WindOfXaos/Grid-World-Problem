"""
search(intial_state):
	#node{ state , path , .. }
	initialize fringe with intital state
	while fringe is not empty :
		pick a node from the fringe according to a strategy
		--if visited : continue
		if goal : return solution
		from state get possible actions
		from actions generate next states
		append successors to the fringe
	return failure 
"""


def get_min(fringe, key):
    min_idx = 0
    for i in range(1, len(fringe)):
        if fringe[i][key] < fringe[min_idx][key]:
            min_idx = i
    return min_idx


def init_node(strategy, intial_state):
    initial_node = {}
    initial_node['state'] = intial_state
    initial_node['path'] = []
    if strategy in ('UCS', 'Astar'):
        initial_node['cost'] = 0
    if strategy == 'Greedy':
        initial_node['h'] = 0
    if strategy == 'Astar':
        initial_node['f'] = 0
    return initial_node


def select_node(strategy, fringe):
    if strategy == 'DFS':
        return -1
    if strategy == 'BFS':
        return 0
    if strategy == 'UCS':
        return get_min(fringe, 'cost')
    if strategy == 'Greedy':
        return get_min(fringe, 'h')
    if strategy == 'Astar':
        return get_min(fringe, 'f')


def add_node(strategy, next_state, action, current_node, compute_cost, heuristic):
    next_node = {}
    next_node['state'] = next_state
    next_node['path'] = current_node['path'][:]
    next_node['path'].append(action)
    if strategy in ('UCS', 'Astar'):
        next_node['cost'] = current_node['cost'] + \
            compute_cost(current_node['state'], action)
    if strategy == 'Greedy':
        next_node['h'] = heuristic(next_node['state'])
    if strategy == 'Astar':
        next_node['f'] = next_node['cost']+heuristic(next_node['state'])
    return next_node


def solve(strategy, intial_state, get_actions, get_state, isgoal, compute_cost=None, heuristic=None):
    fringe = []
    visited = []
    fringe.append(init_node(strategy, intial_state))

    while len(fringe) > 0:
        current_node = fringe.pop(select_node(strategy, fringe))
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        if isgoal(current_node['state']):
            Solution = {}
            Solution['solution'] = current_node['path']
            if strategy in ('UCS', 'Astar'):
                Solution['cost'] = current_node['cost']
            Solution['expanded_nodes'] = len(visited)
            return Solution
        possible_actions = get_actions(current_node['state'])
        for action in possible_actions:
            next_state = get_state(current_node['state'], action)
            next_node = add_node(strategy, next_state,
                                 action, current_node, compute_cost, heuristic)
            fringe.append(next_node)
    return 'failure'
