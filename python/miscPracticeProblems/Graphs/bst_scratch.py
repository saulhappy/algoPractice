from binary_search_tree import BST

    #         10
    #        /   \
    #       5     12
    #     /   \      \
    #    3      7      14 
    #                /    \
    #              13       20

t = BST()
t.insert(10)
t.insert(5)
t.insert(12)
t.insert(3)
t.insert(7)
t.insert(14)
t.insert(13)
t.insert(20)

print(t.get_dfs_preorder_values(t.root))
# [10, 5, 3, 7, 12, 14, 13, 20]
