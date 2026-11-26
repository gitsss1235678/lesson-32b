class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None 

class DoublyLL:
    def __init__(self):
        self.head = None

    def delete_beg(self):
        if self.head !=None:
            Var = self.head
            self.head = self.head.next
            self.head.prev = None
            Var = None

    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            Var = self.head
            while Var:
                print(Var.data, "-->", end = " ")
                Var = Var.next

l = DoublyLL
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n2.prev = n1
n1.next = n2
l.display()
print(end='\n')
l.delete_beg()
l.display()
print(end='\n')
l.delete_end()
l.display()