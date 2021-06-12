# given a binary search tree, count how many nodes are greater than the root's value


    #         10
    #        /   \
    #       5     12
    #     /   \      \
    #    3      7      14 


from binary_search_tree import BST

T = BST()
T.insert(10)
T.insert(5)
T.insert(12)
T.insert(3)
T.insert(7)
T.insert(14)

T.print_tree_inOrder()

def is_greater_root(T):
    pass

