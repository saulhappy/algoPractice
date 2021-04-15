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
        if self.root:
            self._print_tree(self.root)
        
    def _print_tree(self, current_node):
        if current_node:
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
            return self._get_node(value, self.root)
        else:
            return None
    
    def _get_node(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left != None:
            return self._get_node(value, current_node.left)
        elif value > current_node.value and current_node.right != None:
            return self._get_node(value, current_node.right)
        else:
            print(f"A node with the value of {value} is not found in this tree")
            return None
        
    # returns the node with min value in tree rooted at input node
    def min_value_node(self, n):
        current = n
        while current.left != None:
            current = current.left
        return current


    # returns max value of tree
    def max_value(self):
        if self.root != None:
            return self._max_value(self.root)
    
    def _max_value(self, current_node):
        if current_node.right is None:
            print(f"The max value in tree is {current_node.value}")
            return None
        return self._max_value(current_node.right)
    
    # returns max value of tree
    def min_value(self):
        if self.root:
            return self._min_value(self.root)
    
    def _min_value(self, current_node):
        if current_node.left is None:
            print(f"The min value in tree is {current_node.value}")
            return None
        return self._min_value(current_node.left)

    # returns the number of children of input node
    def num_children(self, n):
        num_children = 0
        if n.left != None: num_children +=1
        if n.right != None: num_children += 1
        return num_children

    # deletes node with input value
    def delete_value(self, value):
        if self.root:
            return self._delete_node(self.root, value)
        print("The tree is empty. Nothing to delete")
        return None

    def _delete_node(self, current_node, value):
        if current_node.value == value:
            # leaf node:
            if not current_node.left and not current_node.right: return None
            # node has one right child:
            if not current_node.left and current_node.right: return current_node.right
            # node has one left child:
            if not current_node.right and current_node.left: return current_node.left
            # node has two children:
            if current_node.right and current_node.left: print("figuring it out")

        if current_node.value > value:
            current_node.left = self._delete_node(current_node, value)
        else:
            current_node.right = self._delete_node(current_node, value)

        return current_node

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
tree.insert(12)


print("   ")
print(f"tree's nodes are: ")
tree.print_tree_inOrder()
print("   ")
print("tree's height is: ", tree.height())
print("tree's node count is", tree.count)
tree.max_value()
tree.min_value()

# current delete implementation: https://www.youtube.com/watch?v=wMyWHO9F1OM
# STILL NOT WORKING! >:/

# print("   ")
# tree.delete_value(5)
# print(f"tree's nodes are: ")
# tree.print_tree_inOrder()
# print("   ")
# print("tree's node count is", tree.count)
