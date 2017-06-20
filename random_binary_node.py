from math import log

class BinaryTree
    def __init__(self,data):
        self.root = Node(data)
        self.size =1
    def insert(self,data):
        self.root.insert(Node(data))
        self.size += 1
    def get_random_node(self):

        return


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,node):
        if node.data < self.data:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

bst = BinaryTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(100)
bst.insert(30)
bst.insert(2)
bst.insert(150)
bst.insert(-2)
bst.insert(-20)
bst.insert(4)

if __name__ == "__main__":

