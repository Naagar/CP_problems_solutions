# stack using lined list

# pop()
# push()
# is_empty()
# 
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None
        # self.tail = None
class stack:
    def __init__(self):
        self.lined_list = linked_list()
    
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False
    def push(self, value):
        node = Node()
        node.next = self.lined_list.head
        self.lined_list.head = node
    def pop(self):
        if self.is_empty:
            return 'empty stack'
        else:
            node_value = self.lined_list.value
            self.lined_list.head = self.lined_list.head.next
            return node_value 
    def peek(self):
        if self.is_empty:
            return 'empty stack'
        else:
            node_value = self.lined_list.head.value

            return node_value
    # def delete(self):


custm_stack = stack()
print(custm_stack.is_empty())