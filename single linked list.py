class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        
class Linkedlist:
    def __init__(self):
       self.Head=None
    
    
    def insert(self,val):
        if(not self.Head):
            new_node=Node(val)
            self.Head=new_node
        else:
            temp=self.Head
            while(temp.next):
                temp=temp.next
            new_node=Node(val)
            temp.next=new_node
        print("{} is successfully inserted".format(val))
    def display(self):
        res=[]
        temp=self.Head
        while(temp):
            res.append(temp.data)
            temp=temp.next
        print("--->".join(map(str,res)))    
            
            
l=Linkedlist()           
l.insert(100)
l.insert(200)
l.insert(300)
l.insert(400)
l.display()