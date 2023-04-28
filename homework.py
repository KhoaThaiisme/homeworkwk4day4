from Node import Node


def insert_node(value, node= None):
    if not node:
        node = Node(value)
    if value < node.value:
        if not node.left:
            node.left = Node(value)
        else:
            return insert_node(value, node.left)
    else:
        if not node.right: 
            node.right = Node(value)
        else:
            return insert_node(value, node.right)
def to_bts(alist):
    node = None
    for value in alist:
        node = insert_node(value)
    return node

def binary_decorator(func):
    def wrapper(alist):
        node = to_bts(alist)
        return func(node)
    return wrapper

@binary_decorator
def get_min(alist):
    if not node:
        node = Node(value)
        return node.value
    return get_min(node.left)


lst = [3, 7, 2, 8, 1, 9, 4, 6, 5]
result = get_min(lst)
print(result)  # Output: 1
