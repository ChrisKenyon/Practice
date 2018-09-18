"""
    My A* algorithm example
"""

import heapq
import pdb

class Cell(object):
    def __init__(self,x,y,reachable):
        """
        Init new cell
        @param x cell x coordinate
        @param y cell y coordinate
        @param reachable is cell reachable? not wall?
        """
        self.x = x
        self.y = y
        self.reachable = reachable
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

class AStar(object):
    def __init__(self):
        self.open = []
        heapq.heapify(self.open)
        self.close = set()
        self.cells = []
        self.grid_h = 6
        self.grid_w = 6
        self.init_grid()

    def init_grid(self):
        walls = ((0,5),(1,0),(1,1),(1,5),(2,3),(0,3),
                 (3,1),(3,2),(3,5),(4,1),(4,4),(5,1))
        for x in range(self.grid_h):
            for y in range(self.grid_w):
                reach = (x,y) not in walls
                self.cells.append(Cell(x,y,reach))
        self.start = self.get_cell(0,0)
        self.end = self.get_cell(5,5)

    def get_heuristic(self,cell):
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y-self.end.y))

    def get_cell(self,x,y):
        return self.cells[x*self.grid_h + y]

    def get_adj_cells(self,cell):
        cells=[]
        if cell.x < self.grid_w-1:
            cells.append(self.get_cell(cell.x+1,cell.y))
        if cell.y > 0:
            cells.append(self.get_cell(cell.x,cell.y-1))
        if cell.x > 0:
            cells.append(self.get_cell(cell.x-1,cell.y))
        if cell.y < self.grid_h-1:
            cells.append(self.get_cell(cell.x,cell.y+1))
        return cells

    def display_path(self):
        cell = self.end
        while cell.parent is not self.start:
            cell = cell.parent
            print 'cell: {} {}'.format(cell.x,cell.y)

    def update_cell(self,adj,cell):
        adj.g = cell.g+10
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def process(self):
        # add start cell to queue. heap sorts by f value (first in tuple)
        heapq.heappush(self.open, (self.start.f, self.start))
        while self.open:
            # pop cell
            f, cell = heapq.heappop(self.open)
            # add cell to closed
            self.close.add(cell)
            if cell is self.end:
                self.display_path()
                return
            adj_cells = self.get_adj_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.close:
                    if (adj_cell.f,adj_cell) in self.open:
                        # if in open, check if this path is better
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell,cell)
                    else:
                        self.update_cell(adj_cell,cell)
                        # add to open
                        heapq.heappush(self.open, (adj_cell.f,adj_cell))
        print "No path!"


if __name__=='__main__':
    algorithm = AStar()
    algorithm.process()
    pass
