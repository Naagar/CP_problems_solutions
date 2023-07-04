# stack_list
class stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return 'pushed'

    def pop(self):
        if self.is_empty():
            return 'empty'
        else:
            return self.list.pop()
    def peek(self):
        if self.is_empty:
            return 'empty'
        else:
            return self.list[len(self.list)-1]

cust_stack = stack()
cust_stack.push(1)
cust_stack.push(2)
cust_stack.push(3)
cust_stack.push(4)

print(cust_stack.pop())
print('ablbs')
print(cust_stack)
