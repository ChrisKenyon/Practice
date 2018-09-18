class Node:
    def __init__(self):
        self._parent = self
    @property
    def parent(self):
        if self._parent != self:
            return self._parent.parent
        else:
            return self
    @parent.setter
    def parent(self, val):
        if self._parent != self and self.parent != val.parent:
            self._parent.parent = val
            return self.parent
        else:
            self._parent = val
            return val

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M) #4
        forest = [Node() for i in range(N)]  #[Node()]*4
        for i in range(N-1):  # 0 -> 2]
            node1 = forest[i]  # Node 0
            for j in range(i+1, N):  # 0 -> 3]
                node2 = forest[j]
                if bool(M[i][j]):
                    node2.parent = node1
        return len([node for node in forest if node.parent == node])


if __name__ == '__main__':
    solve = Solution()
    solve.findCircleNum([[1,1,1],[1,1,1],[1,1,1]])

