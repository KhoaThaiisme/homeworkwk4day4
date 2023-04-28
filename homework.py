from BST import BinarySearchTree
"""
    create function take in a func which take in a list wrapper -> convert list to bst
"""

def convert_to_bst(func):
    def wrapper(alist):
        bst = BinarySearchTree(alist[0])
        for e in alist[1:]:
            bst.add_node(e)
        func(bst)
    return wrapper

@convert_to_bst
def print_bst(alist):
    alist.print_in_order()
    return

print_bst([10,4,19,11,100])