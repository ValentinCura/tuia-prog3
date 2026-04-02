from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
        grid (Grid): Grid of points

        Returns:
        Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)

        # TODO Complete the rest!!
        # ...
        while True:
            if frontier.is_empty(): return False
            n = frontier.remove()
            for a in grid.actions(n.state):
                if a not in grid.actions(n.state): continue
                s = grid.result(n.state, a)
                if s in reached: continue
                else:
                    np = Node("", s, n.cost + grid.individual_cost(n.state, a), n, a)
                    if grid.objective_test(s): return Solution(np, reached)
                    reached[s] = True
                    frontier.add(np)

        return NoSolution(reached)