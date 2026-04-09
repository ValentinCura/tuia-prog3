from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        node = root
        frontier = PriorityQueueFrontier() #creo una cola de prioridad
        frontier.add(node, grid.calculate_distance(node)) #agrego el nodo inicial a la cola 

        while not frontier.is_empty(): 

            node = frontier.pop() 

            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                sucesor = grid.result(node.state, action)            
                nuevocosto = node.cost + grid.individual_cost(node.state, action)

                if sucesor not in reached or nuevocosto < reached[sucesor]:
                    nodo_hijo = Node("", sucesor, cost=nuevocosto, parent=node, action=action)
                    frontier.add(nodo_hijo, grid.calculate_distance(nodo_hijo))
                    reached[nodo_hijo.state] = nodo_hijo.cost

        return NoSolution(reached)
