
from random import randint
class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
class LL:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next
    def __str__(self):

        values = [str(x.value) for x in self]
        return ' --> '.join(values)
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node    = node.next
        return result
    def add(self, value):
        if self.head is None:
            new_node = node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = node(value)
            self.tail = self.tail.next
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
        
# custom_ll = LL()
# custom_ll.generate(10, 0, 9)
# print(custom_ll)
# print(len(custom_ll))


# remove duplicates

def remove_dups(ll):
    if ll.head is None:
        return
    else:
        curr_node = ll.head
        visited_node = set([curr_node.value])
        while curr_node.next:
            if curr_node.next.value in visited_node:
                curr_node.next = curr_node.next.next
            else:
                visited_node.add(curr_node.next.value)
                curr_node = curr_node.next
        return ll
custom_ll = LL()
custom_ll.generate(10, 0, 10)
print(custom_ll)
remove_dups(custom_ll)
print(custom_ll)

# curr_node = node_1
# temp_set = {}
# while cur_node.next is not None:
#     if 
# # # 