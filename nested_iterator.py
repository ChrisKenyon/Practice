import pdb
#pdb.set_trace()
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.next_loaded = None
        self.nlist = nestedList
        self.generator = self.gen()

    def gen(self):
        def y_next(subl):
            for elem in subl:
                while self.next_loaded:
                    yield self.next_loaded
                if isinstance(elem, list):
                    yield from y_next(elem)
                else:
                    yield elem
        yield from y_next(self.nlist)
        if self.next_loaded:
            val = self.next_loaded
            self.next_loaded = None
            yield val

    def next(self):
        """
        :rtype: int
        """
        res = next(self.generator)
        self.next_loaded = None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            test = self.next()
        except StopIteration:
            return False
        if test:
            self.next_loaded = test
            return True
        return False


if __name__ == "__main__":
    nested_iter = NestedIterator([1,[4,[6]]])
    print(nested_iter.hasNext())
    print(nested_iter.hasNext())
    print(nested_iter.next())
    print(nested_iter.hasNext())
    print(nested_iter.hasNext())
    print(nested_iter.hasNext())
    print(nested_iter.next())
    print(nested_iter.hasNext())
    print(nested_iter.next())
    print(nested_iter.hasNext())
    print(nested_iter.hasNext())
