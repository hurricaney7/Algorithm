import math


def get_distance(point_1, point_2):
    return math.sqrt(math.pow((point_1[0] - point_2[0]), 2) + math.pow((point_1[1] - point_2[1]), 2))


def remove_best(frontiers, f_costs):
    frontiers_cost = {}
    for el in frontiers:
        frontiers_cost[f_costs[el]] = el
    min_key = min(frontiers_cost.keys())
    return frontiers_cost[min_key]


def build_path(came_from, cur):
    path = [cur]
    while cur in came_from.keys():
        cur = came_from[cur]
        path.insert(0, cur)
    return path


def shortest_path(M, start, goal):
    # Actual path cost
    g_costs = {}

    # Total path cost
    f_costs = {}

    # Initial g cost and f cost for start node
    g_costs[start] = 0
    f_costs[start] = get_distance(M.intersections[start], M.intersections[goal]) + g_costs[start]

    # Nodes that have been explored
    explored = []

    # Edge nodes to be explored
    frontiers = [start]

    # which node the current node is from
    came_from = {}

    while len(frontiers) != 0:
        cur_node = remove_best(frontiers, f_costs) if remove_best(frontiers, f_costs) > 0 else start
        if cur_node == goal:
            return build_path(came_from, goal)

        if cur_node in frontiers:
            frontiers.remove(cur_node)

        if cur_node not in explored:
            explored.append(cur_node)

        # Put all frontiers of current node in
        for i in range(len(M.roads[cur_node])):
            neighbor = M.roads[cur_node][i]
            # If the neighbor is already explored, skip this one
            if neighbor in explored:
                continue
            # If the neighbor is not added to frontiers yet, add it
            if neighbor not in frontiers:
                frontiers.append(neighbor)

            g = g_costs[cur_node] + get_distance(M.intersections[cur_node], M.intersections[neighbor])
            if neighbor in g_costs.keys() and g >= g_costs[neighbor]:
                continue

            came_from[neighbor] = cur_node
            g_costs[neighbor] = g
            f_costs[neighbor] = g + get_distance(M.intersections[neighbor], M.intersections[goal])

