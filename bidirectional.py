from collections import deque

def bidirectional_bfs(maze):
    start = maze.start
    end = maze.end
    width = maze.width
    total_nodes = width * maze.height

    # Visited sets for both directions
    visited_from_start = [False] * total_nodes
    visited_from_end = [False] * total_nodes

    # Parent trackers for both directions
    prev_from_start = [None] * total_nodes
    prev_from_end = [None] * total_nodes

    # Queues for BFS
    queue_from_start = deque([start])
    queue_from_end = deque([end])

    visited_from_start[start.Position[0] * width + start.Position[1]] = True
    visited_from_end[end.Position[0] * width + end.Position[1]] = True

    def construct_path(meeting_node):
        path = deque()
        current = meeting_node
        while current:
            path.appendleft(current)
            current = prev_from_start[current.Position[0] * width + current.Position[1]]

        current = prev_from_end[meeting_node.Position[0] * width + meeting_node.Position[1]]
        while current:
            path.append(current)
            current = prev_from_end[current.Position[0] * width + current.Position[1]]

        return path

    count = 0
    completed = False

    while queue_from_start and queue_from_end:
        count += 1

        # BFS step from the start
        current_from_start = queue_from_start.popleft()
        for neighbor in current_from_start.Neighbours:
            if neighbor:
                pos = neighbor.Position[0] * width + neighbor.Position[1]
                if not visited_from_start[pos]:
                    visited_from_start[pos] = True
                    prev_from_start[pos] = current_from_start
                    queue_from_start.append(neighbor)

                    if visited_from_end[pos]:
                        completed = True
                        return [construct_path(neighbor), [count, len(construct_path(neighbor)), completed]]

        # BFS step from the end
        current_from_end = queue_from_end.popleft()
        for neighbor in current_from_end.Neighbours:
            if neighbor:
                pos = neighbor.Position[0] * width + neighbor.Position[1]
                if not visited_from_end[pos]:
                    visited_from_end[pos] = True
                    prev_from_end[pos] = current_from_end
                    queue_from_end.append(neighbor)

                    if visited_from_start[pos]:
                        completed = True
                        return [construct_path(neighbor), [count, len(construct_path(neighbor)), completed]]

    return [deque(), [count, 0, completed]]  # No path found

def solve(maze):
    return bidirectional_bfs(maze)
