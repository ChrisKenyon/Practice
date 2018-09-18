from waypoint import Waypoint

from Queue import Queue
from itertools import product, starmap
import pdb

class PathFinder(object):

    def get_path(self, grid, start_wp, end_wp):
        """Returns a list of Waypoints from the start Waypoint to the end Waypoint.
:
        :param grid: Grid is a 2D numpy ndarray of boolean values. grid[x, y] == True if the cell contains an obstacle.
        The grid dimensions are exposed via grid.shape
        :param start_wp: The Waypoint that the path should start from.
        :param end_wp: The Waypoint that the path should end on.
        :return: The path from the start waypoint to the end waypoint that follows the movement model without going
        off the grid or intersecting an obstacle.
        :rtype: A list of Waypoints.

        More documentation at
        https://docs.google.com/document/d/1b30L2LeKyMjO5rBeCui38j_HSUYgEGWXrwSRjB7AnYs/edit?usp=sharing
        """




        ''' Naive BFS solution to validate shortest path '''
        def get_valid_neighbors(wp, visited):
            # probably should be in waypoint
            # TODO: comment
            # get all the surrounding tuples to the waypoint
            cells = starmap(lambda a,b: (wp.x+a, wp.y+b), product((0,-1,+1), (0,-1,+1)))
            # check is x in bounds, y in bounds, no obstacle
            check = lambda w: 0 <= w[0] < grid.shape[0] and \
                              0 <= w[1] < grid.shape[1] and \
                              not grid[w[0], w[1]] and \
                              (w[0],w[1]) not in visited
            # return a waypoint for each valid neighbor, except self (result of product 0 0)
            for x,y in filter(check, cells):
                yield Waypoint(x,y,0)

        def backtrack_path():
            # TODO: comment
            # use temp2 for cleanup
            temp = temp2 = end_wp
            path = []
            while temp:
                path.append(temp)
                temp = temp.prev
                del temp2.prev
                temp2 = temp
            return path[::-1]

        # Simple BFS with parent pointers
        search_queue = Queue()
        start_wp.prev = None
        search_queue.put(start_wp)
        visited = set(((start_wp.x,start_wp.y),))
        while not search_queue.empty():
            wp = search_queue.get()
            if wp == end_wp:
                end_wp.prev = wp.prev
                return backtrack_path()
            for neighbor in get_valid_neighbors(wp, visited):
                visited.add((neighbor.x,neighbor.y))
                neighbor.prev = wp
                search_queue.put(neighbor)
        #pdb.set_trace()
        return []
        ''' '''
