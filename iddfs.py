from collections import deque

def depth_limited_search(node, maze, limit, visited, prev):
    if node == maze.end:
        return True
    if limit <= 0:
        return False

    visited[node.Position[0] * maze.width + node.Position[1]] = True
    for neighbor in node.Neighbours:
        if neighbor and not visited[neighbor.Position[0] * maze.width + neighbor.Position[1]]:
            prev[neighbor.Position[0] * maze.width + neighbor.Position[1]] = node
            if depth_limited_search(neighbor, maze, limit - 1, visited, prev):
                return True
    return False

def solve(maze):
    start = maze.start
    end = maze.end
    width = maze.width
    height = maze.height

    max_depth = maze.count  # Limit to the total number of nodes in the maze
    visited = [False] * (width * height)
    prev = [None] * (width * height)
    count = 0
    completed = False

    for depth in range(max_depth):
        visited = [False] * (width * height)
        if depth_limited_search(start, maze, depth, visited, prev):
            completed = True
            break
        count += 1

    # Reconstruct the path
    path = deque()
    current = end
    while current:
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
