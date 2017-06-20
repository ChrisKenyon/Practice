'''

Chris Kenyon

" Find all k-sum descending paths from any node to any lower node in its tree "

'''

import unittest

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def find_k_sums(k,root):
    sums = find_sums(root)
    answer = []
    for key,v in sums.iteritems():
        if v == k:
            answer.append(key)
    return answer

def find_sums(root):
    sums = {(root.data,):root.data}
    if not root.left and not root.right:
        return sums
    rsums,lsums = {},{}
    if root.right:
        rsums = find_sums(root.right)
        rsums.update({(root.data,)+k:v+root.data for k,v in rsums.iteritems()})
    if root.left:
        lsums = find_sums(root.left)
        lsums.update({(root.data,)+k:v+root.data for k,v in lsums.iteritems()})
    sums.update(rsums)
    sums.update(lsums)
    return sums

class KSumTests(unittest.TestCase):
    tree = Node(10)
    tree.left = Node(15)
    tree.left.left = Node(-5)
    tree.right = Node(5)
    tree.right.left = Node(5)
    tree.right.right = Node(20)
    def test_list(self):
        print find_sums(self.tree)
    def test_sums10(self):
        print "10: "
        print find_k_sums(10,self.tree)
    def test_sums20(self):
        print "20: "
        print find_k_sums(20,self.tree)

if __name__ == "__main__":
    unittest.main()
    '''
    import pdb
    pdb.set_trace()
    t = KSumTests()
    t.test_one()
    '''
