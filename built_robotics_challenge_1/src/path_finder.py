from waypoint import Waypoint

from Queue import Queue
import heapq
import sys
MAX_INT = sys.maxint

class KeyedMinHeap(object):
    """This is a OOD version of the python heapq, modified to add
        a key function that allows an objects to be keyed on a lambda,
        and to add a set that allows for constant lookup and gets"""
    def __init__(self, key=lambda x:x, init=[]):
        self.key = key
        self._arr = [(key(data), data) for data in init]
        heapq.heapify(self._arr)
        self.queue_set = set(init)

    def push(self, data):
        self.queue_set.add(data)
        heapq.heappush(self._arr, (self.key(data), data))

    def pop(self):
        data = heapq.heappop(self._arr)[1]
        return data

    def empty(self):
        return len(self._arr) == 0

    def contains(self, data):
        return data in self.queue_set

    def get(self, data):
        # The queue set was implemented so that this constant lookup could be achieved
        # The set a&b function has a performance of O(min(len(a), len(b))), which is always 1 here
        # We are doing this so that we return the object with the correct reference in the heap
        return list(self.queue_set&set((data,)))[0] if data in self.queue_set else None

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

        def get_valid_neighbors(wp, visited=set()):
            """Returns a generator to produce neighbor Waypoints to the given Waypoint wp

            :param wp: Waypoint to find neighbors of
            :param visited: A set of Waypoints to exclude from the return
            :return: The neighbor Waypoint(s) to Waypoint wp that have not been visited in a graph search function
            :rtype: generator<Waypoint>
            """
            # 0 North, 1 East, 2 South, 3 West
            MOVES = {
                0 : {0:(0,1), 45:(-1,1), 135:(-1,-1),180:(0,-1),225:(1,-1), 315:(1,1)},
                1 : {0:(1,0), 45:(1,1),  135:(-1,1), 180:(-1,0),225:(-1,-1),315:(1,-1)},
                2 : {0:(0,-1),45:(1,-1), 135:(1,1),  180:(0,1), 225:(-1,1), 315:(-1,-1)},
                3 : {0:(-1,0),45:(-1,-1),135:(1,-1), 180:(1,0), 225:(1,1),  315:(-1,1)}
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
                            Waypoint(wp.x+change_xy[315][0],wp.y+change_xy[315][1],(wp.orientation + 1) % 4)] # 315 deg (fwr-r)

            # check is x in bounds, y in bounds, no obstacle
            check = lambda w: 0 <= w.x < grid.shape[0] and \
                              0 <= w.y < grid.shape[1] and \
                              not grid[w.x, w.y] and \
                              w not in visited
            # return a waypoint for each valid neighbor, except self (result of product 0 0)
            for neighbor in filter(check, all_neighbors):
                neighbor.f = neighbor.g = neighbor.h = MAX_INT
                yield neighbor

        def backtrack_path():
            """Uses the end_wp and prev attribute to trace a path from start_wp to end_wp
               Also cleans up the created attributes from the A* algorithm
            :return: A list of waypoints that represents the path start to finish if the chain
                      of Waypoints was accurately created
            :rtype: list<Waypoint>
            """
            temp = temp2 = end_wp
            path = []
            while temp:
                path.append(temp)
                temp = temp.prev

                # clean up attributes used for this algorithm
                del temp2.prev,
                if hasattr(temp2, 'h') and hasattr(temp2, 'g') and hasattr(temp2,'f'):
                    del temp2.h, temp2.f, temp2.g
                temp2 = temp
            return path[::-1]

        ''' Iteration 1 for validation --
        # Simple BFS with parent pointers -- O(V+E) complexity
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
        '''

        # A* algorithm with naive heuristic

        def get_heuristic(wp):
            """This is a naive heuristic just taking into account the Euclidean distance
               This could be extended to account for orientation and field-practical
                straight vs. backward vs. diagonal edge costs & a variety of other factors
               Doing so could prioritize forward movement and remove some of the silly
               looking diagonals in the result paths"""
            return abs(wp.x - end_wp.x) + abs(wp.y - end_wp.y)
        def update_wp(neighbor,wp):
            """Increment g, h, and f scores of the neighbor based on the prev waypoint"""
            neighbor.g = wp.g+1
            neighbor.h = get_heuristic(neighbor)
            neighbor.f = neighbor.h + neighbor.g
            neighbor.prev = wp

        # f, g, h, prev could've (and probably should've) been initialized in Waypoint,
        # but I'll keep my modifications confined to this file
        start_wp.g = end_wp.f = end_wp.g = end_wp.h = 0
        start_wp.f = start_wp.h = get_heuristic(start_wp)
        start_wp.prev = None

        # add start wp to queue. heap sorts by f value (first in tuple)
        min_queue = KeyedMinHeap(lambda x: x.f, (start_wp,))
        finished = set()

        while not min_queue.empty():  # O(V)
            # Get the waypoint with the current lowest f score
            wp = min_queue.pop() # O(logV)
            # only add to visited when popped off min queue to be sure it was min
            finished.add(wp)

            # if our end was found at the top of the min heap, we know we've found the path
            if wp == end_wp:
                end_wp.prev = wp.prev
                return backtrack_path()

            # Try to find the neighbors with the next lowest f scores
            for neighbor in get_valid_neighbors(wp, finished): # In one iteration constant O(6), but O(E) overal
                q_neighbor = min_queue.get(neighbor) # Constant lookup using set (O(1)), rather than always push O(logV)
                if q_neighbor:
                    # check if this path is better (like dijkstra)
                    if q_neighbor.g > wp.g + 1:
                        update_wp(q_neighbor,wp)
                else:
                    update_wp(neighbor,wp)
                    # Add to queue as potential..
                    min_queue.push(neighbor) # O(logV)
        # If there's no path, return an empty path
        return []
'''

 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 EXPLANATION

 While a simple BFS has a better complexity on paper, A* is a better algorithm to use here - not only
 for its speed increase, but also because it is extendable for realistic applications of Mary Anne the robot.
 It is likely that moving diagonally, switching directions, acceleration, and other various factors result
 in movements between the grid cells that are not all exactly equal cost, and A* is extendable to factor
 those things in later on, while still being practically faster in this application (I'm seeing ~0.033s for
 all tests with A* vs. ~0.185s with BFS on my laptop).
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 COMPLEXITY

 V == grid.shape[0] * grid.shape[1] * 4 orientations, E = # valid adjacency edges
 In this 2D grid, E <= 6 * V, given each V has a max of 6 possible connections (less on average),
 technically meaning O(V) == O(E)

 The space used is O(V) for each of the key heap's array, key heap's set, and finished set

 The queue while loop gives a worst case time of V, and the checks of all neighbors
 across that worst case V waypoints results in a worst case time of E.
 In each of these blocks, a log(V) operation is performed - pop and push respectively.
 This results in a O((V + E)logV) worst case complexity. (Could be slightly better with fib heap)
 This can be simplified to O(VlogV) considering O(V) == O(E)

 Other representations of time complexity are often more informative than the standard use of V and E,
 e.g. the AI community uses a better time complexity for an algorithm which is the
 branching factor, b, to the power of the depth of the end node, d, for a complexity of O(b^d)

 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''


