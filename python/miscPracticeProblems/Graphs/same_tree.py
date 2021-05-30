"""
source: https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""

from binary_search_tree import BST

p = BST()
p.insert(17)
p.insert(12)
p.insert(25)
p.insert(9)
p.insert(21)
p.insert(27)

q = BST()
q.insert(17)
q.insert(12)
q.insert(25)
q.insert(9)
q.insert(21)
# q.insert(27)


def isSameTree(p, q):
    # algo1
    # def fn(p, q): 
    #     """Return True if trees rooted at p and q are structurally identical"""
    #     if not p or not q: return p is q
    #     return fn(p.left, q.left) and p.value == q.value and fn(p.right, q.right)
    
    # return fn(p, q)


    # algo2
    if not p and not q:return True
    if not p and q:return False
    if not q and p:return False
    if p.value != q.value:return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

print(isSameTree(p.root, q.root))

