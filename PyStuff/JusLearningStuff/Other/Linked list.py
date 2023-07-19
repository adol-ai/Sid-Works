class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,NewData):
        NewNode=Node(NewData)
        NewNode.next=self.head
        self.head=NewNode

    def PrintAll(self):
        temp=self.head
        while (temp):
            print(temp.data, end=" ")
            temp=temp.next

l_l=LinkedList()
l_l.push(7)
l_l.push(47)
l_l.push(77)

l_l.PrintAll()
