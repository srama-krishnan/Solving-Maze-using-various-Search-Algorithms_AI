import math
import random
from collections import deque

def simulated_annealing(maze):
    start = maze.start
    end = maze.end
    width = maze.width
    height = maze.height

    def heuristic(node):
        # Manhattan distance heuristic
        return abs(node.Position[0] - end.Position[0]) + abs(node.Position[1] - end.Position[1])

    def get_all_neighbors(node, visited):
        # Return all valid neighbors that haven't been visited
        return [neighbor for neighbor in node.Neighbours if neighbor and neighbor not in visited]

    current = start
    path = deque([current])
    max_restarts = 50  # Number of restarts to escape local minima
    temperature = 100  # Higher initial temperature for medium-scale mazes
    cooling_rate = 0.98  # Slower cooling rate for better exploration
    visited = set()
    count = 0
    completed = False

    for _ in range(max_restarts):
        current = start
        path = deque([current])
        visited = set()
        temperature = 100

        while temperature > 1:
            count += 1
            if current == end:
                completed = True
                break

            visited.add(current)
            neighbors = get_all_neighbors(current, visited)

            if not neighbors:
                # Backtrack if no valid neighbors are available
                if len(path) > 1:
                    path.pop()
                    current = path[-1]
                continue

            next_node = random.choice(neighbors)  # Randomly select a neighbor
            delta_e = heuristic(current) - heuristic(next_node)

            # Accept the move if it's better or with some probability if it's worse
            if delta_e > 0 or math.exp(delta_e / temperature) > random.random():
                path.append(next_node)
                current = next_node

            temperature *= cooling_rate  # Reduce the temperature

        if completed:
            break  # Exit if a solution is found

    # If the goal was not reached, return an empty path
    if not completed:
        path = deque()

    return [path, [count, len(path), completed]]

def solve(maze):
    return simulated_annealing(maze)
