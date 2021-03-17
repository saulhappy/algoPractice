# custom implementation of binary search tree

class Node():
    def __init__(self, value = None):
        self.value = value
        self.right = None
        self.left = None

class BST():
    def __init__(self):
        self.root = None
        self.count = 0


    # if there is no root, create it, increment the count. else, call private insert with the value. 
    # private methods should not be called outside of the class
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            self.count += 1
        else:
            self._insert(value, self.root)
            self.count += 1
    
    # recursive private insert method:
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = Node(value)
            else: 
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else:
            print("This value is already in the tree")
            self.count -= 1

    def print_tree_inOrder(self):
        if self.root != None:
            self._print_tree(self.root)
        
    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left)
            print(str(current_node.value))
            self._print_tree(current_node.right)


def fill_tree(tree, num_elems=10, max_int=100):
    from random import randint

    while num_elems > 0:
        value = randint(0, max_int)
        tree.insert(value)
        num_elems -= 1
    return tree



tree = BST()
tree = fill_tree(tree)
tree.print_tree_inOrder()

print(f"The tree has {tree.count} elements")