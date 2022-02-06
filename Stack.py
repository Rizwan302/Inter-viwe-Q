# write a stack class
# create stack class object named back_history for back history
# create stack class object named forward_history for forward history
# open link1, then link2, then link3
# go back two times
# go forward two times.
from inspect import stack


class Stack():
    def __init__(self):
        self.my_stack = []
    def put_item(self, item):
        self.my_stack.append(item)
    def pop_item(self):
        self.my_stack.pop()
    def value_item(self):
        if self.my_stack == []:
            print("Stack is empty")
    def dis(self):
        print(self.my_stack)
        
        
a = Stack()
a.put_item(1)
a.put_item(2)
a.put_item(3)
a.put_item(4)
a.put_item(5)
a.put_item(6)
a.put_item(7)
a.put_item(8)
a.put_item(9)
a.put_item(10)
a.pop_item()
a.pop_item()
a.dis()


    

