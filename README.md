# Solving-Maze-using-various-Search-Algorithms_AI

This repository contains Python implementations of various maze-solving algorithms. The objective of this project is to explore and analyze different algorithms for solving mazes and to provide a toolkit for users to experiment with them.

For any queries or feedback, feel free to reach out at **sramakrishnan1841@gmail.com**.

---

## Table of Contents
- [About the Project](#about-the-project)
- [Algorithms Implemented](#algorithms-implemented)
- [Installation](#installation)
- [Usage Instructions](#usage-instructions)
- [Maze Input Guidelines](#maze-input-guidelines)
- [Notes and Considerations](#notes-and-considerations)

---

## About the Project
This project provides implementations of multiple algorithms for solving mazes, each with its unique characteristics and use cases. It serves as a resource for learning, experimentation, and comparison of various search and optimization techniques in maze-solving.

---

## Algorithms Implemented
The following algorithms are included in this repository:
1. **A* Algorithm** (`astar.py`): Combines heuristics and path cost to find the optimal path.
2. **Bidirectional Search** (`bidirectional.py`): Searches simultaneously from the start and end points to find the shortest path.
3. **Breadth-First Search** (`breadthfirst.py`): Explores all possible paths level by level.
4. **Depth-First Search** (`depthfirst.py`): Explores one path deeply before backtracking.
5. **Dijkstra’s Algorithm** (`dijkstra.py`): Finds the shortest path from a source node using edge weights.
6. **Iterative Deepening Depth-First Search** (`iddfs.py`): Combines depth-first and breadth-first searches by limiting search depth.
7. **Simulated Annealing** (`simulatedannealing.py`): Probabilistically optimizes the path using a cooling schedule.
8. **Left Turn Algorithm** (`leftturn.py`): Simple algorithm that follows walls to find a way out.

Additional utilities, such as Fibonacci heaps (`FibonacciHeap.py`) and priority queues (`priority_queue.py`), are included to enhance algorithm performance.

---

## Installation
Follow these steps to set up the project on your local machine:

1. Clone the repository:
```bash
git clone https://github.com/your-username/maze-solving-algorithms.git
cd maze-solving-algorithms
```
2. Create a virtual environment and activate it:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Usage Instructions
To run the maze-solving algorithms, use the `solve.py` script with the following command structure:

```bash
python solve.py -m <algorithm> <input_image_path> <output_image_path>
```

Command-Line Arguments:
-m <algorithm>: Specify the maze-solving algorithm to use. Replace <algorithm> with one of the following:
- astar
- bidirectional
- breadthfirst
- depthfirst
- dijkstra
- iddfs
- simulatedannealing
- leftturn

## Maze Input Guidelines
To ensure compatibility, input maze images must follow these rules:

The maze must be black and white:
- White (RGB: 255, 255, 255) represents paths.
- Black (RGB: 0, 0, 0) represents walls.
- The maze must be surrounded by a black border.

There must be exactly one white square at the top row (starting point) and one white square at the bottom row (ending point).

Example mazes are included in the **images** directory.

## Notes and Considerations
- **Efficiency and Memory Usage**:  
  Large mazes may consume significant memory. Ensure you have sufficient RAM, especially for high-resolution mazes.

- **Algorithm Performance**:  
  The performance of each algorithm depends on the maze structure. For example:
  - Dense mazes with short paths may favor simpler algorithms like BFS.
  - Sparse mazes with longer paths may benefit from A* or Dijkstra.

- **Scalability**:  
  Algorithms like Simulated Annealing are computationally expensive and may not perform well on large mazes.
