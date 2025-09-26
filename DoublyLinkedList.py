class Node : 
    def __init__(self,data,next=None,prev=None):
        self.data=data 
        self.next=next 
        self.prev=prev
    def __repr__(self):
        return f'{self.data}'
    
class LinkedList : 
    def __init__(self,initial_values=None):
        self.head=None 
        self.tail=None 
        self.length=0 
        if initial_values : 
            for value in initial_values : 
                self.insert_end(value)
   
   
    def _add_node(self, node):
        self.debug_data.append(node)
        self.length += 1

    def print (self): 
        cur=self.head 
        while cur : 
            print (cur.data,end="->") 
            cur=cur.next
        print ("None")
    
    def print_reversed(self): 
        cur=self.tail 
        while cur is not None : 
            print (cur.data , end="->")
            cur=cur.prev 
        print('None')

    ##################################################
    @staticmethod
    def _link( first , second ): 
        if first : 
            first.next=second 
        if second: 
            second.prev=first 

    def insert_end(self,value) : 
        node = Node(value)
        if not self.head : 
            self.head=self.tail=node 
        else : 
            self._link(self.tail,node)
            self.tail=node 
    
    def insert_front(self,value): 
        node=Node(value)
        self._link(node,self.head) 
        self.head=node 
        if self.length == 1 : 
            self.head=node 


#################################################
lst = LinkedList([1, 2, 3, 4, 5])
lst.insert_front(20)
lst.print()
