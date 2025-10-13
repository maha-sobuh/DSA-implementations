#array-based stack 
class Stack : 
    def __init__(self):
        self.items=[]
    def push (self,item):
        self.items.append(item) 
    def pop(self): 
        assert self.items, 'No items!'
        return self.items.pop() 
    def peek(self): 
        assert self.items, 'No items!'
        return self.items[-1]
    def isEmpty(self):
        return len(self.items)==0
    def size(self): 
        return len(self.items)
    

################################################## 
s = Stack()
print(s.peek())
