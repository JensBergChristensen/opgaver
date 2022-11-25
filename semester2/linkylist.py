# linked list experiment

from distutils.log import ERROR


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def print(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
    def find(self, index):
        current = self.head
        try:
            for i in range(index):
                current = current.next
        except(AttributeError) as e:
            print(e)
        return current

item = LinkedList()
item.insert(1)
item.insert(2)
item.insert(3)
item.insert(400)
item.insert("hello")
item.insert(42)
item.insert(True)
item.insert("hejsa")
ting = item.find(4)

item.print()
print("index item:",ting.value)
