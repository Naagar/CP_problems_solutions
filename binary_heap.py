# binary_heap.py

class heap:
    def __init__(self, size):
        self.custom_list = (size+1) * [None]
        self.heap_size = 0
        self.max_size = size + 1

def peek_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.custom_list[1]
def size_heap(root_node):
    if not root_node:
        return
    else: 
        return root_node.heap_size
def level_order_travers(root_node):
    if not root_node:
        return
    else:
        for i in range(1, root_node.heap_size + 1):
            print(root_node.custom_list[i])
def heapify(root_node, index, heap_type):
    parent_index = int(index/2)
    if index <= 1:
        return
    if heap_type == 'Min':
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify(root_node, parent_index, heap_type)
    if heap_type == 'Max':
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify(root_node, parent_index, heap_type)
def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
        return 'the Binary heap iws full'
    root_node.custom_list[root_node.heap_size + 1] = node_value 
    root_node.heap_size += 1
    heapify(root_node, root_node.heap_size, heap_type)
    return 'the vlue hab been successfulluy inserted'

def heapify_and_extract(root_node, index, heap_type):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0

    if root_node.heap_size == left_index:
        return
    elif root_node.heap_size == left_index:
        if heap_type == 'Min':
            if root_node.custom_list[index] > root_node.custom_list[index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp 
            return 
        else:
            if root_node.custom_list[index] < root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
    else:
        if heap_type == 'Min':
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[swap_child] = temp 
        else:
            if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
                swap_child = left_index
            else: 
                swap_child = right_index
            if root_node.custom_list[index] < root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[swap_child]
                root_node.custom_list[swap_child] = temp 
def extract_node(root_node, heap_type):
    if root_node.heap_size == 0:
        return
    else:
        extract_node = root_node.custom_list[1]
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
        root_node.custom_list[root_node.heap_size] = None
        root_node.heap_size -= 1
        heapify_and_extract(root_node, 1, heap_type)
        return extract_node
def delete_binary_heap(root_node):
    root_node.custom_list = None




new_binary_heap = heap(5)
insert_node(new_binary_heap, 4, 'Max')
insert_node(new_binary_heap, 3, 'Max')
insert_node(new_binary_heap, 2, 'Max')
insert_node(new_binary_heap, 1, 'Max')
insert_node(new_binary_heap, 6, 'Max')
level_order_travers(new_binary_heap)
print(new_binary_heap)