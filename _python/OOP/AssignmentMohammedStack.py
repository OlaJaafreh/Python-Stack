class Stacknode:
    def __init__(self, val, next= None):
        self.val = val
        self.next = next



    

class MinStack:

    def __init__(self):
        self.top = None
        self.size = 0
        self.min_stack = []

    def push(self, val):
        newnode = Stacknode(val)
        if not self.top:
            self.top = newnode
            self.min_stack.append(newnode)
        
        else:
            curr = self.top
            newnode.next =curr
            self.top = newnode
            if self.top.val <= self.min_stack[-1].val:
                self.min_stack.append(newnode)
        self.size += 1
        

    def pop(self):
        if not self.top:
            return
        else:
            if self.top == self.min_stack[-1]:
                self.min_stack.pop()
            curr = self.top.next
            self.top.next = None
            self.top = curr
        
        self.size -= 1
        

    def gettop(self):
        if not self.top:
            return
        else:
            return self.top.val
    
    def getmin(self):
        return print(f"The Minimum Value = " + str(self.min_stack[-1].val))

    def printList(self):
                if not self.top:
                    return
                current = self.top
                while current:
                    print(current.val, end="")
                    if current.next:
                        print(" --> ", end="")
                    current = current.next
                print(" --> null")


stack1 = MinStack()
stack1.push(-10)
stack1.push(2)
stack1.push(-13)
stack1.push(5)
stack1.push(-15)
stack1.pop()
print(stack1.gettop())


stack1.printList()

stack1.getmin()

