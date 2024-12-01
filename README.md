# Solving-Maze-using-various-Search-Algorithms_AI

This repository contains Python implementations of various maze-solving algorithms. The objective of this project is to explore and analyze different algorithms for solving mazes and to provide a toolkit for users to experiment with them.

---

## Table of Contents
- [About the Project](#about-the-project)
- [Algorithms Implemented](#algorithms-implemented)
- [Installation](#installation)
- [Usage Instructions](#usage-instructions)
- [Maze Input Guidelines](#maze-input-guidelines)
- [Notes and Considerations](#notes-and-considerations)
- [License](#license)
- [Contributing](#contributing)

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

