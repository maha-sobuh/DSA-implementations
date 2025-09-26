class Node : 
    def __init__(self,data,next=None,prev=None):
        self.data=data 
        self.next=next 
        self.prev=prev
    def __repr__(self):
        return f'{self.data}'

