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
    def _link( first , second ): #used just inside the class 
        if first : 
            first.next=second 
        if second: 
            second.prev=first 
    
    def _delete_and_link(self,node): ##used just inside the class
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

    def delete_node_with_key(self,key): 
        if not self.length : 
            return 
        if self.head.data == key : 
            self.delete_front()
        else : 
            cur = self.head 
            while cur : 
                if cur.data == key : 
                    self._delete_and_link(cur) 
                    break
                cur=cur.next 
    ##########################  Problems : 
    def delete_all_with_key(self,key) : 
        if not self.length : 
            return  
        self.insert_front (key-1)
        cur = self.head 
        while cur.data==key : 
            self.delete_front()
            cur=self.head
        while cur : 
            if cur.data == key : 
                self._delete_and_link(cur) 
            cur=cur.next 
        self.delete_front()

    def delete_even_positions(self) : 
        if self.length<=1  : 
            return 
        cur = self.head 
        while cur and cur.next : 
            self._delete_and_link(cur.next) 
            cur=cur.next

    def delete_odd_positions(self): ## reuse previous methods 
        self.insert_front(-1) 
        self.delete_even_positions() 
        self.delete_front() 

    def is_palindrome(self): 
        start,end=self.head,self.tail 
        leng=self.length //2 
        while leng:
            if start.data != end.data : 
                return False 
            end=end.prev 
            start=start.next
            leng-=1
        
        return True
    
    #### find the middle without using length veriable 
    def get_middle(self) : 
        l , r = self.head , self.tail 
        while l : 
            if l == r or r.next==l : 
                return l
            r=r.prev 
            l=l.next 
        return
    
    ### find the middle without using prev , length 
    ## solve using Tortoise and the Hare Algorithm 
    def get_middle2(self): 
        t , h = self.head , self.head 
        while h and h.next : 
            t=t.next 
            h=h.next.next 
        return t 
    
    ### Given k , swap the kth node form the front with the kth node from the back 
    def swap_kth(self,k): 
        if k>self.length: 
            return 
        first , second = self.head , self.tail 
        for i in range(k-1): 
            first=first.next 
            second=second.prev 
        
        next1 , prev1 = first.next , first.prev 
        next2,prev2 = second.next , second.prev 
        if first.next == second : 
            self._link(first , next2)
            self._link(prev1,second)
            self._link(second,first) 
        else:
            self._link(second,next1)
            self._link(prev1,second)
            self._link(prev2,first)
            self._link(first,next2)
        if k == 1 or k==self.length : 
            self.head , self.tail = self.tail , self.head 
    
    ### Given a list , reverse all its nodes (addresses)
    def reverse(self): 
        if self.length <=1 : 
            return 
        cur , nxt = self.head , self.head.next 
        while cur : 
            cur.next , cur.prev= cur.prev , cur.next 
            cur=nxt 
            if nxt:
                nxt=nxt.next 
        self.head , self.tail = self.tail , self.head 


#################################################
# lst = LinkedList([1, 2, 3, 4, 5])
# print(lst.length )
# lst.insert_front(20)
# lst.print()
# print(lst.length)
# lst2 = LinkedList([1, 5,10,20])
# print (lst2.length)
# lst2.delete_last()
# lst2.print()
# print (lst2.length) 
lst3 = LinkedList([10,10,10,10]) 
# lst3.delete_node_with_key(10)
# lst3.print()
# lst3.delete_all_with_key(10)
# lst3.print()
# lst4 = LinkedList([1,7,9,3])
# lst4.delete_odd_positions()
# lst4.print()
lst5 = LinkedList([1,3,5,6,7,9])
# print(lst5.is_palindrome())
# print (lst5.get_middle())
# print(lst5.get_middle2())
# lst5.swap_kth(2)
# lst5.print()
lst5.reverse()
lst5.print()


