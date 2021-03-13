# custom implementation of binary search tree

class Node():
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None

class BST():
    def __init__(self):
        self.root = None
        self.count = 0


    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            self.count += 1
    

