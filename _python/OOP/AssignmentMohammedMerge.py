class Node:
    def __init__(self,data,next=None):
        self.data=data;
        self.next=next;

class LinkedList:

            def __init__(self):
                self.head=None;
                self.size=0;

            def get(self,index):
                if index<0 or index>self.size:
                    return "Out of bound"
                current = self.head
                for i in range(index):
                    current=current.next
                return print(current.data)

            def AddAtHead(self,data):
                if self.head==None:
                    self.head = Node(data)
                    self.size+=1
                    return 
                else:
                    temp = self.head
                    self.head = Node(data)
                    self.head.next = temp
                    self.size+=1

            def AddAtTail(self,data):
                NewNode = Node(data)
                if self.head==None:
                    self.head = NewNode
                    self.size+=1
                    return 
                else:
                    current = self.head
                    while current.next:
                        current=current.next
                    current.next = NewNode
                    NewNode.next=None
                    self.size+=1

            def AddAtIndex(self,data,index):
                if index<0 or index>self.size:
                    return "Out of bound"
                NewNode = Node(data)
                if self.head==None:
                    self.head = NewNode
                    self.size+=1
                    return 
                else:
                    current = self.head
                    for i in range(index-1):
                        current=current.next
                    temp=current.next
                    current.next = NewNode
                    NewNode.next=temp
                    self.size+=1

            def DeleteAtIndex(self,index):
                if index<0 or index>self.size:
                    return "Out of bound"
                if self.head==None:
                    return
                if index==0:
                    temp=self.head
                    self.head = self.head.next
                    temp.next=None
                else:
                    current = self.head
                    for i in range(index-1):
                        current=current.next
                    temp=current.next
                    current.next = current.next.next
                    temp.next=None
                    self.size-=1


            def MergeNorm(self,List2):
                if List2.head==None:
                    return
                if self.head==None:
                    self.head=List2.head
                    return
                current = self.head
                while current.next:
                        current=current.next
                current.next = List2.head


            def MergeZegZag(self,List2):
                if List2.head==None:
                    return
                if self.head==None:
                    self.head=List2.head
                    return
                current1=self.head
                current2=List2.head
                while current1 and current2:
                        temp1=current1.next
                        temp2=current2.next
                        current1.next = current2
                        current2.next = temp1
                        current1=temp1
                        current2=temp2
                return self
            
            def rev(self):
                prev = None
                current= self.head
                while current:
                      nextcur = current.next
                      current.next = prev
                      prev = current
                      current=nextcur
                #self.head.next = None
                self.head = prev


            def printList(self):
                current = self.head
                while current:
                    print(current.data, end="")
                    if current.next:
                        print(" --> ", end="")
                    current = current.next
                print(" --> null")

            
                        

SLL = LinkedList()
SLL.AddAtHead("Mahmoud")
SLL.AddAtTail("Jaafreh")
SLL.AddAtHead("Ola")
SLL.printList()

SLL1 = LinkedList()
SLL1.AddAtHead(140)
SLL1.AddAtTail(1400)
SLL1.AddAtHead(540)
SLL1.printList()


#SLL.MergeNorm(SLL1)
#SLL.printList()

SLL.MergeZegZag(SLL1)
SLL.printList()

SLL1.printList()
SLL1.rev()
SLL1.printList()
