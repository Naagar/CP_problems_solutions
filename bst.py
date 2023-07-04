# binary search tree
from queue_using_list import queue
class bst_node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert(root_node, value):
    if root_node.data == None:
        root_node.data = value
    elif value <= root_node.data:
        if root_node.left_child is None:

            root_node.left_child = bst_node(value)
        else:
            insert(root_node.left_child, value)
    else:
        if root_node.right_child is None:
            root_node.right_child = bst_node(value)
        else:
            insert(root_node.right_child, value)
    return 'node is successfully inserted'
def pre_order_travers(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_travers(root_node.left_child)
    pre_order_travers(root_node.right_child)
def post_order_travers(root_node):
    if not root_node:
        return 
    pre_order_travers(root_node.left_child)
    pre_order_travers(root_node.right_child) 
    print(root_node.data)

def in_order_travers(root_node):
    if not root_node:
        return
    in_order_travers(root_node.left_child)
    print(root_node.data)
    in_order_travers(root_node.right_child)
def level_order_travers(root_node):
    if not root_node:
        return
    else:
        custom_queue = queue(10)
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            print(root.data)
            if root.left_child is not None:
                custom_queue.enqueue(root.left_child)
            if root.right_child is not None:
                custom_queue.enqueue(root.right_child)


def bst_search(root_node, value):
    # if root_node is None:
    #     return 'bst empty'
    if root_node.data == value:
        return 'element exist'
    elif  value < root_node.data :
        if root_node.left_child.data == value:
            print('the value is found')
        else:
            bst_search(root_node.left_child, value)
    else:
        if root_node.right_child.data == value:
            print('value found')
        else:
            bst_search(root_node.right_child, value)

def min_value(bst_node_value):
    current = bst_node_value
    while (current.left_child is not None):
        current = current.left_child
    return current

def delet_node(root_node, value):
    if root_node is None:
        return root_node
    if value < root_node.data:
        root_node.left_child = delet_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delet_node(root_node.right_child, value)
    else:
        if root_node.left_child is None:
            temp = root_node.left_child
            root_node = None
            return temp 
        if root_node.right_child is None:
            temp = root_node.right_child
            root_node = None
            return temp 
        temp = min_value(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delet_node(root_node.right, temp.data)
    return root_node
def delet_bst(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "bst is deleted"

new_bst = bst_node(None)
insert(new_bst, 40)
insert(new_bst, 60)
insert(new_bst, 80)
insert(new_bst, 700)
insert(new_bst, 30)
insert(new_bst, 20)
# pre_order_travers(new_bst)
# post_order_travers(new_bst)
# in_order_travers(new_bst)
# level_order_travers(new_bst)
# bst_search(new_bst, 700)
# delet_node(new_bst, 700)
delet_bst(new_bst)
