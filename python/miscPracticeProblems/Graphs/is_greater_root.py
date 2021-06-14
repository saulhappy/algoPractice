# given a binary search tree, count how many nodes are greater than the root's value


    #         10
    #        /   \
    #       5     12
    #     /   \      \
    #    3      7      14 
    #                /    \
    #              13       20

from binary_search_tree import BST

t = BST()
t.insert(10)
t.insert(5)
t.insert(12)
t.insert(3)
t.insert(7)
t.insert(14)
t.insert(13)
t.insert(20)

tree_root_value = t.root.value
def is_greater_root(node):
    if node is None: return 0
    count = 0

    count = is_greater_root(node.left)
    count += 1
    count += is_greater_root(node.right)

    return count

print(is_greater_root(t.root.right))