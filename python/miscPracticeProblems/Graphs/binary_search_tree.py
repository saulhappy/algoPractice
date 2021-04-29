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


    # if there is no root, create it, increment the count. else, call private insert with the value. 
    # private methods should not be called outside of the class
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
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

    def print_tree_inOrder(self):
        if self.root:
            self._print_tree(self.root)
        
    def _print_tree(self, current_node):
        if current_node:
            self._print_tree(current_node.left)
            print(str(current_node.value))
            self._print_tree(current_node.right)


    def count_nodes(self):
        if self.root:
            return self._count_nodes(self.root)
        else:
            return None
        
    def _count_nodes(self, current_node):
        left_count = 0
        right_count = 0

        if current_node.left is None and current_node.right is None: return 1      
        if current_node.left: left_count = self._count_nodes(current_node.left)
        if current_node.right: right_count = self._count_nodes(current_node.right)

        return left_count + right_count + 1

# CALCULATE HEIGHT OF TREE

    # ALGO 1
    # def height(self):
    #     if self.root != None:
    #         return self._height(self.root, 0)
    #     else:
    #         return 0

    # def _height(self, current_node, current_height):
    #     if current_node == None: return current_height
    #     left_height = self._height(current_node.left, current_height + 1)
    #     right_height = self._height(current_node.right, current_height + 1)
    #     return max(left_height, right_height)

    #ALGO 2
    def height(self):
        if self.root:
            return self._height(self.root)
        else:
            return None

    def _height(self, current_node):
        left_height = 0
        right_height = 0
        if current_node.left is None and current_node.right is None: return 1
        if current_node.left: left_height = self._height(current_node.left)
        if current_node.right: right_height = self._height(current_node.right)
        
        return max(left_height, right_height) + 1

# TRAVERSALS

    #DFS: IN ORDER: LEFT, ROOT, RIGHT
    # ALGO 1
    # def get_dfs_inorder_values(self):
    #     values = []
    #     if self.root: 
    #         self._get_dfs_inorder_values(self.root, values)
    #         return values
    #     else:
    #         return None
    
    # def _get_dfs_inorder_values(self, current_node, values):
    #     if current_node.left: self._get_dfs_inorder_values(current_node.left, values)
    #     values.append(current_node.value)
    #     if current_node.right: self._get_dfs_inorder_values(current_node.right, values)
    #     return values   
    # 
    
    # ALGO 2:
    def get_dfs_inorder_values(self, node):
        values = []
        if node is None: return []
        if node.left: values += self.get_dfs_inorder_values(node.left)
        values.append(node.value)
        if self.root.right: values += self.get_dfs_inorder_values(node.right)
        return values 
    
    #DFS: PRE ORDER: ROOT, LEFT, RIGHT
    # [ 15, 10, 3, 17, 16, 22 ]
    def get_dfs_preorder_values(self, node):
        values = []
        if node is None: return []
        values.append(node.value)
        if node.left: values += self.get_dfs_preorder_values(node.left)
        if node.right: values += self.get_dfs_preorder_values(node.right)
        return values


    #DFS: POST ORDER: LEFT, RIGHT, ROOT
    def get_dfs_postorder_values(self, node):
        values = []
        if node is None: return []
        if node.left: values += self.get_dfs_postorder_values(node.left)
        if node.right: values += self.get_dfs_postorder_values(node.right)
        values.append(node.value)
        return values

    # BFS: USING A QUEUE TO DO LEVEL ORDER TRAVERSAL

    def get_bfs_values(self):
        values = []
        queue = []
        if self.root is None: return None
        queue.append(self.root)

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node.left: queue.append(current_node.left)
            if current_node.right: queue.append(current_node.right)
            values.append(current_node.value)
        return values

    def sum_nodes(self):
        if self.root is None: return 0
        return self._sum_nodes(self.root)
    
    def _sum_nodes(self, current_node):
        left_sum = 0
        right_sum = 0

        if current_node.left is None and current_node.right is None: return current_node.value
        if current_node.left: left_sum = self._sum_nodes(current_node.left)
        if current_node.right: right_sum = self._sum_nodes(current_node.right)

        return current_node.value + left_sum + right_sum


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
        if self.root is None: 
            print("This tree is empty.")
            return None
        self._delete_node(self.root, value)
   

    def _delete_node(self, current_node, value):
        if current_node is None: return None

        if current_node.value == value:
            # node has no children
            if current_node.left is None and current_node.right is None: return None
            # node only has right child
            if current_node.left is None and current_node.right: return current_node.right
            # node only has left child
            if current_node.left and current_node.right is None: return current_node.left
            # node has both children: replace node's value with next min value
            if current_node.left and current_node.right: 
                pointer = current_node.right
                while pointer.left: pointer = pointer.left # keep traversing left to get lowest value
                current_node.value = pointer.value # copy value
                current_node.right = self._delete_node(current_node.right, current_node.value)# delete node of value we copied

        if current_node.value > value:
            current_node.left = self._delete_node(current_node.left, value)
        else:
            current_node.right = self._delete_node(current_node.right, value)
        
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
tree.insert(3)
tree.insert(9)
tree.insert(20)
tree.insert(15)
tree.insert(7)

print(f"tree's nodes are: ")
tree.print_tree_inOrder()
print(f"sum of left leaves: {tree.sum_left_leaves(tree.root)}")
