'''
Chris Kenyon

"Create a generator that produces the next closest point to the origin"

'''


import sys

class CoordGraph:
    ''' A class specifically designed for starting from the origin and
        generating the next closest Euclidean points on a graph '''
    def next_tier(self):
        ''' Each group of coordinates is made up of a potential 8
            coordinate groups, which is all 2-permutations of 2 numbers
            and their negatives created in an incrementing pattern where
            the difference in the sum of the squares is minimized which
            each step '''
        first = 0
        second = 0
        while True:
            # probably could do this nicer with itertools...
            set_ = set([(first,second),
                        (second,first),
                        (first,-second),
                        (-second,first),
                        (-first,second),
                        (second,-first),
                        (-first,-second),
                        (-second,-first)])
            if first == second:
                first += 1
                second = 0
            else:
                second += 1
            yield list(set_)
    def next_coord(self):
        ''' This is a generator function to give next closest (or equally)
            coordinate point to the origin of a 2D Euclidean coordinate plane.
            Somewhat reminiscent of a breadth first search, although uses
            the modified next tier generator to build the queue rather than
            looking for neighbors (as it would be more trouble than necessary
            to build a graph. Simply pulls from the queue until next tier. '''
        tier_gen = self.next_tier()
        queue = tier_gen.next()
        while queue:
            s = queue.pop(0)
            # No need for a 'visited' hash set as with BFS, as the tier will be unique
            if len(queue) == 0:
                queue = tier_gen.next()
            yield s


if __name__ == "__main__":
    ''' Give an argument of how many coordinates you would like printed '''
    num = int(sys.argv[1])
    searcher = CoordGraph()
    coord_gen = searcher.next_coord()
    for i in range(num):
        print coord_gen.next(),
