# given a binary search tree, count how many node values are even


    #         10
    #        /   \
    #       5     12
    #     /   \      \
    #    3      6      14 
    #   /
    #  2

from binary_search_tree import BST

t = BST()
t.insert(10)
t.insert(5)
t.insert(12)
t.insert(3)
t.insert(6)
t.insert(14)
t.insert(2)
# should return 5

def count_even_values(node):
    if node is None: return 0
    
    count = 0 

    count = count_even_values(node.left)
    if node.value % 2 == 0: count += 1
    count += count_even_values((node.right))

    return count
    

print(count_even_values(t.root))