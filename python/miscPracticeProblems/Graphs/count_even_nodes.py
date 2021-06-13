# given a binary search tree, count how many node values are even


    #         10
    #        /   \
    #       5     12
    #     /   \      \
    #    3      6      14 


from binary_search_tree import BST

t = BST()
t.insert(10)
t.insert(5)
t.insert(12)
t.insert(3)
t.insert(6)
t.insert(14)

t.print_tree_inOrder()

def is_even_value(t):
    pass 

print(is_even_value(t))