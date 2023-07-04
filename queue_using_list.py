# queue_using_list

# enqueue, dequeue, start end 
# is_Full()
 
# is_empty()

# Circular queue
# from _typeshed import StrPath

class queue:
    def __init__(self, max_size):
        self.items    = max_size * [None]
        self.max_size = max_size
        self.start    = -1
        self.top      = -1
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    # def 
    def enqueue(self, value):
        if self.is_full():
            return 'queue is full'
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
        return 'inserted'
    def dequeue(self):
        if self.is_empty():
            return 'empty queue'
        else:
            frist_el = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return frist_el
    def peek(self):
        if self.is_empty():
            return 'empty queue'
        else:
            return self.items[self.start]
    def delete(self):
        self.items = self.max_size * [None]
        self.top = -1
        self.start = -1

# custom_quese = queue(3)
# custom_quese.enqueue(3)
# custom_quese.enqueue(3)
# custom_quese.enqueue(3)

# print(custom_quese)
# custom_quese.dequeue()
# print(custom_quese)
# print(custom_quese.peek())
# custom_quese.delete()
