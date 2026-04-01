from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...

        frontier = StackFrontier()
        frontier.add(root)

        while True:
            if frontier.is_empty():
                return NoSolution(expanded)
            node = frontier.remove()
            if node.state in expanded:
                continue
            expanded[node.state] = True
            for action in grid.actions(node.state):
                node_after_action = grid.result(node.state,action)
                if node_after_action not in expanded:
                    node2 = Node("",state=node_after_action,parent=node,action=action,cost=node.cost + grid.individual_cost(node.state,action))
                    if grid.objective_test(node2.state):
                        return Solution(node2,reached=expanded)
                    frontier.add(node2)

