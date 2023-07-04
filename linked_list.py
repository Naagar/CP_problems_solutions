# Linked_list 
# create head and tails and connect them
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
class single_ll:
    def __init__(self):
        self.head = None
        self.tail = None

s_LL = single_ll()
node1 =Node(1)
node2 = Node(2) 
node3 = Node(3)


single_ll.head = node1
single_ll.head.next = node2
single_ll.tail = node2

# insert node in LL at head, middle, end

single_ll.head = node3
single_ll.node3.next = node1

single_ll.head.next = node3
single_ll.node3.next = node2

print(single_ll.tail)

def traverNode(self):
    if self.head is None:
        print("linked list does not exist")
    else:
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

# def node():

def search_ll(self, node_value):
    if self.head is None:
        return 'list does not exist'
    else:
        node = self.head
        while node is not None:
            if node.value == node_value:
                    
                node = self.value == node_value
            return node.value
        return 'The value does not exist'

# def LL():

# deleting nodes in LL

# def delete_node(self, location):
#     if self.node is None:
#         return 'll does not exist'
#     else:
#         if location == 0:
#             if self.head == self.tail:
#                 self.head = None
#                 self.tail = None
#             else:
#                 self.head = self.head.next
#         elif location == 1:
#             if self.head == self.tail:
#                 self.head = None
#                 self.tail = None
#             else:
#                 node = self.head
#                 while node is not None:
#                     if node.next == self.tail:
#                         break
#                     node = node.next
#                 node.next = None
#                 self.tail = node
#             else:
#                 tempNode = self.head
#                 index = 0
#                 while index < location - 1:
#                     tempNode = tempNode.next
#                     index += 1
#                 nextNode = traverNode.next
#                 tempNode.next = nextNode.next


# deleting LL
def delet_ll(self):
    if self.head in None:
        print('The SSL does not exist')
    else:
        self.head = None
        self.tail = None 