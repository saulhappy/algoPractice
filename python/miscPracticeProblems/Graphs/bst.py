# custom implementation of binary search tree

class Node():
    def __init__(self, value = None):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

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
                current_node.left.parent = current_node
            else: 
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = Node(value)
                current_node.right.parent = current_node
            else:
                self._insert(value, current_node.right)
        else:
            print(f"{value} is already in the tree")
            self.count -= 1

    def print_tree_inOrder(self):
        if self.root != None:
            self._print_tree(self.root)
        
    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left)
            print(str(current_node.value))
            self._print_tree(current_node.right)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None: return current_height
        left_height = self._height(current_node.left, current_height + 1)
        right_height = self._height(current_node.right, current_height + 1)
        return max(left_height, right_height)

    def contains(self, value):
        if self.root != None:
            return self._contains(self.root, value)
        else:
            return False

    def _contains(self, current_node, value):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left != None:
            return self._contains(current_node.left, value)
        elif value > current_node.value and current_node.right != None:
            return self._contains(current_node.right, value)
        return False 

    def get_node(self, value):
        if self.root != None:
            return self._get_node(self.root, value)
    
    def _get_node(self, current_node, value):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left != None:
            return self._get_node(current_node.left, value)
        elif value > current_node.value and current_node.right != None:
            return self._get_node(current_node.right, value)
        
    def delete_value(self, value):
        return self.delete_node(self.get_node(value))

    def delete_node(self, node):
        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current

        # returns the number of children of input node
        def num_children(n):
            num_children = 0
            if n.left != None: num_children +=1
            if n.right != None: num_children += 1
            return num_children

        # get the parent of the node to be deleted, and num of child nodes
        node_parent = node.parent
        node_children_num = num_children(node)

        # break deletion operation into different cases based on the
        # tree's structure and node targeted for deletion

        # CASE 1: node has no leaves: simply set parent's reference of
        # that node to none

        if node_children_num == 0:
            if node_parent.left == node:
                node_parent.left == None
            else:
                node_parent.right == None 

        # CASE 2: node has a single child: swap out the parent of that child, with the parent of the node. 

        if node_children_num == 1:
            # get that single child
            if node.left != None:
                child = node.left
            else:
                child = node.right
            # replace targeted node for deletion with its single child. 
        if node_parent.left == node:
            node_parent.left = child
        else:
            node_parent.right = child



# helper function to fill tree in with random integers
def rand_fill_tree(tree, num_elems=10, max_int=100):
    from random import randint

    while num_elems > 0:
        value = randint(0, max_int)
        tree.insert(value)
        num_elems -= 1
    return tree

# tree = rand_fill_tree(tree)

tree = BST()
tree.insert(7)
tree.insert(5)
tree.insert(8)
tree.insert(3)
tree.insert(6)
tree.insert(20)
tree.insert(15)
tree.insert(23)
tree.insert(23)
tree.print_tree_inOrder()

print(f"The tree has {tree.count} elements")
print(f"the tree's height is {tree.height()}")
print(tree.contains(7))
print(tree.contains(17))
print(tree.contains(15))
print(tree.contains(23))

print(tree.get_node(12))