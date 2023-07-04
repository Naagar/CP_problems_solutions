# binary_tree
# Depth frist search
# Breadth frist search

# Pre order traversal root,left, right
# Post-order traversal, left right, root
# In-order traversal, left, root, right
from queue_using_list import queue
class tree_node:
    def __init__(self, data):
        self.data        = data
        self.left_child  = None
        self.right_child = None

new_BT = tree_node('drinks')
print(new_BT)
def pre_order_travers(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_travers(root_node.left_child)
    pre_order_travers(root_node.right_child)

def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)

def post_order_travers(root_node):
    if not root_node:
        return
    post_order_travers(root_node.left_child)
    post_order_travers(root_node.right_child)
    print(root_node.data)
def lever_order_travers(root_node):
    if not root_node:
        return
    else:
        custom_queue = queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            print(root_node.data)
            if (root.value.left_child is not None):
                custom_queue.enqueue(root.value.left_child)
            
            if (root.value.right_child is not None):
                custom_queue.enqueue(root.value.right_child)
def search_bt(root_node, node_l):
    if not root_node:
        return 'BT does not exit'
    else:
        custom_queue = queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty):
            root = custom_queue.dequeue()
            if root.value.data == node_l:
                return True 
            if (root.value.left_child is not None):
                custom_queue.enqueue(root.value.left_child)
            if (root.value.right_child is not None):
                custom_queue.enqueue(root.value.right_child)
        return 'Not found' 