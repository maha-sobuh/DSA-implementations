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
    
    def _delete_and_link(self,node): 
        if not node : 
            return 
        isTail= node==self.tail
        prev=node.prev 
        self._link(prev,node.next)
        self.length-=1 
        if isTail : 
            self.tail=prev

    def insert_end(self,value) : 
        node = Node(value)
        if not self.head : 
            self.head=self.tail=node 
        else : 
            self._link(self.tail,node)
            self.tail=node 
        self.length +=1 
    
    def insert_front(self,value): 
        node=Node(value)
        self.length+=1 
        self._link(node,self.head) 
        self.head=node 
        if self.length == 1 : 
            self.head=node 

    def insert_sorted(self,value) : 
        if self.length==0 or value<=self.head.data: 
            self.insert_front(value)
        elif self.tail.data <=value : 
            self.insert_end(value)
        else : 
            prev , cur = self.head , self.head.next 
            node=Node(value)
            while cur : 
                if value <= cur.data : 
                    self._link(node,cur)
                    self._link(prev,node)
                    self.length +=1 
                    break 
                prev=prev.next 
                cur=cur.next 
    
    def delete_front(self): 
        if not self.head : 
            return 
        next=self.head.next
        self._delete_and_link(self.head)
        self.head=next

        if self.head : 
            self.head.prev=None 
        if self.length<=1 : 
            self.tail=self.head

    def delete_last(self): 
        if self.length <=1: 
            self.delete_front()

        prevu=self.tail.prev
        self.tail=prevu
        self.tail.next=None
        self.length-=1 


#################################################
lst = LinkedList([1, 2, 3, 4, 5])
print(lst.length )
lst.insert_front(20)
lst.print()
print(lst.length)
lst2 = LinkedList([1, 5,10,20])
print (lst2.length)
lst2.delete_last()
lst2.print()
print (lst2.length)


