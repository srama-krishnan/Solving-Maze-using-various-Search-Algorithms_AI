class SolverFactory:
    def __init__(self):
        self.Default = "breadthfirst"
        self.Choices = ["breadthfirst", "depthfirst", "dijkstra", "astar", "leftturn", "iddfs", "bidirectional", "simulatedannealing"]

    def createsolver(self, type):
        if type == "leftturn":
            import leftturn
            return ["Left turn only", leftturn.solve]
        elif type == "depthfirst":
            import depthfirst
            return ["Depth first search", depthfirst.solve]
        elif type == "dijkstra":
            import dijkstra
            return ["Dijkstra's Algorithm", dijkstra.solve]
        elif type == "astar":
            import astar
            return ["A-star Search", astar.solve]
        elif type == "iddfs":
            import iddfs
            return ["Iterative Deepening Depth First Search", iddfs.solve]
        elif type == "bidirectional":
            import bidirectional
            return ["Bidirectional Search", bidirectional.solve]
        elif type == "simulatedannealing":
            import simulatedannealing
            return ["Simulated Annealing Search", simulatedannealing.solve]
        else:
            import breadthfirst
            return ["Breadth first search", breadthfirst.solve]
