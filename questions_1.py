M1 = []
M2 = [
    [6, 9, 5, 4],
    [3, 2, 1, 0],
    [9, 8, 7, 5],
    [2, 5, 6, 9]
]


# DFS iteration
def max_matrix_path_dfs(M, start, goal):
    if not M:
        return 0
    else:
        stack = [start]
        path = []
        while len(stack) != 0:
            cur = stack.pop()
            path.append(M[cur[0]][cur[1]])
            # If comes to the goal point
            if cur[0] == goal[0] and cur[1] == goal[1]:
                print(path)
                path.clear()
            # Append bottom
            if cur[1] + 1 <= len(M[0]) - 1:
                stack.append((cur[0], cur[1] + 1))
            # Append right
            if cur[0] + 1 <= len(M) - 1:
                stack.append((cur[0] + 1, cur[1]))


# DFS Recursion
def max_matrix_path_dfs_recursive(M, start, goal):
    path = recursive_search(M, start, goal)
    return path


def recursive_search(M, cur, goal):
    if cur[0] == goal[0] and cur[1] == goal[1]:
        return [cur]
    else:
        if cur[1] + 1 <= len(M[0]) - 1:
            return recursive_search(M, (cur[0] + 1, cur[1]), goal).append(cur)
        if cur[0] + 1 <= len(M) - 1:
            return recursive_search(M, (cur[0], cur[1] + 1), goal).append(cur)


def max_path_bfs():
    frontiers = []



# max_matrix_path_dfs(M2, (0, 0), (len(M2) - 1, len(M2[0]) - 1))
print(max_matrix_path_dfs_recursive(M2, (0, 0), (len(M2) - 1, len(M2[0]) - 1)))
