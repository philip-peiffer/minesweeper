# This module contains an abstraction for spaces that are neither mines
# or neighbors to mines.
from space import Space
from mine import Mine
from mine_neighbors import MineNeighbor
from collections import deque

class FreeSpace(Space):

    def __init__(self, row, col, board) -> None:
        super().__init__(row, col, board)

    def select(self, event):
        """
        Calls the parent class (space) select method to configure
        display on the current space. Then expands this call 
        outwards to all neighbors.
        """
        
        super().select(event)
        self.__expand_selection(self, event)


    def __expand_selection(self, first_space, event):
        """
        Does BFS expanding outwards performing select
        method on neighbors until a mine neighbor is hit.
        """
        q = deque()
        for neighbor in first_space.neighbors:
            q.append(neighbor)
        
        while len(q) > 0:
            node = q.popleft()
            
            if node.selected:   # node has been visited before
                continue
            elif isinstance(node, Mine):
                continue
            elif isinstance(node, MineNeighbor):
                node.select(event)
                continue

            node.select(event)
            for neighbor in node.neighbors:
                q.append(neighbor)