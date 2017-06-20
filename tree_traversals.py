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

def in_order(root):
    if root:
        in_order(root.left)
        print root.data
        in_order(root.right)

def pre_order(root):
    if root:
        print root.data
        in_order(root.left)
        in_order(root.right)

def post_order(root):
    if root:
        in_order(root.left)
        in_order(root.right)
        print root.data

def breadth_first(root):
    queue = [root]
    while queue:
        n = queue.pop(0) # this is a bad queue
        print n.data
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)

def depth_first(root):
    stack = [root]
    while stack:
        n = stack.pop()
        print n.data
        if n.left:
            stack.append(n.left)
        if n.right:
            stack.append(n.right)

bst = Node(10)
bst.insert(Node(5))
bst.insert(Node(15))
bst.insert(Node(100))
bst.insert(Node(30))
bst.insert(Node(2))
bst.insert(Node(150))
bst.insert(Node(-2))
bst.insert(Node(-20))
bst.insert(Node(4))

print "In Order"
in_order(bst)

print "Pre Order"
pre_order(bst)

print "Post Order"
post_order(bst)

print "Breadth First"
breadth_first(bst)

print "Depth First"
depth_first(bst)
