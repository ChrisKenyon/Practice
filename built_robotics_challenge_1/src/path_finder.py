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

        def get_valid_neighbors(wp, visited):
            '''
            :param wp: Waypoint
            :return: The neighbor Waypoint(s) to Waypoint wp that have not been visited in a graph search function
            :rtype: (Generator function) Waypoint
            '''
            # 0 North, 1 East, 2 South, 3 West
            MOVES = {
                0 : {0:(0,1),45:(-1,1),135:(-1,-1), 180:(0,-1), 225:(1,-1),  315:(1,1)},
                1 : {0:(1,0), 45:(1,1), 135:(-1,1),180:(-1,0),225:(-1,-1), 315:(1,-1)},
                2 : {0:(0,-1), 45:(1,-1),  135:(1,1), 180:(0,1),225:(-1,1),315:(-1,-1)},
                3 : {0:(-1,0),45:(-1,-1), 135:(1,-1),  180:(1,0), 225:(1,1), 315:(-1,1)}
            }
            change_xy = MOVES[wp.orientation]

            # degrees are considering forward direction as the 0 degree
            # reference point. e.g. if north is forward, 0 degrees, then north-west is 45 degrees
            # 90 and 270 deg motion not included (can't move left or right)
            all_neighbors= [Waypoint(wp.x+change_xy[0][0],  wp.y+change_xy[0][1],   wp.orientation),          # 0 deg (fwr)
                            Waypoint(wp.x+change_xy[45][0], wp.y+change_xy[45][1], (wp.orientation - 1) % 4), # 45 deg (fwr-l)
                            Waypoint(wp.x+change_xy[135][0],wp.y+change_xy[135][1],(wp.orientation + 1) % 4), # 135 deg (bck-l)
                            Waypoint(wp.x+change_xy[180][0],wp.y+change_xy[180][1], wp.orientation),          # 180 deg (bck)
                            Waypoint(wp.x+change_xy[225][0],wp.y+change_xy[225][1],(wp.orientation - 1) % 4), # 225 deg (bck-r)
                            Waypoint(wp.x+change_xy[315][0],wp.y+change_xy[315][1],(wp.orientation + 1) % 4)] # 315 deg (bck-r)

            # check is x in bounds, y in bounds, no obstacle
            check = lambda w: 0 <= w.x < grid.shape[0] and \
                              0 <= w.y < grid.shape[1] and \
                              not grid[w.x, w.y] and \
                              w not in visited
            # return a waypoint for each valid neighbor, except self (result of product 0 0)
            for neighbor in filter(check, all_neighbors):
                yield neighbor

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
        visited = set((start_wp,))
        while not search_queue.empty():
            wp = search_queue.get()
            if wp == end_wp:
                end_wp.prev = wp.prev
                return backtrack_path()
            for neighbor in get_valid_neighbors(wp, visited):
                visited.add(neighbor)
                neighbor.prev = wp
                search_queue.put(neighbor)
        return []
