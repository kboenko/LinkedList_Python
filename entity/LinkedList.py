from entity import Node
from utils import deleteItemsByValue as dbv

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, node):
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def find_by_value(self, value):
        node = self.head
        result =[]

        while node != None:
            if node.value == value:
                result.append(node)
            node = node.next

        return result

    def delete_by_value(self, value):
        node = self.head
        prevNode = None

        while node != None:
            if node.value != value:
                prevNode = node
            elif node.value == value and prevNode != None:
                if node.next != None:
                    prevNode.next = node.next
                else:
                    prevNode.next = None
                    self.tail = prevNode
                    self.tail.next = None
                break
            elif node.value == value and prevNode == None:
                node = node.next
                break
        node = node.next

    def clear(self):
        self.head = None
        self.tail = None

    def get_length(self):
        node = self.head
        length = 0

        while node != None:
            if node.value:
                length += 1
            node = node.next
        return length

    def get_values(self):
        node = self.head
        values = []

        while node != None:
            values.append(node.value)
            node = node.next
        return values

    def delete_all_by_value(self, value):
        reducedList = dbv.deleteItemsByValue(self.head, value)
        node = reducedList
        tail = None

        while node != None:
            if node.next == None:
                self.tail = node
            node = node.next

        self.head = reducedList

    def insert_after(self, newNode, nodeNumber):
        node = self.head

        if self.get_length() < nodeNumber:
            print('Введённое значение превышает размер списка!')
        else:
            counter = 0

            while node != None:
                if (counter != nodeNumber):
                    counter += 1

                    if node.next != None:
                        node = node.next
                    else:
                        node.next = newNode
                        break
                else:
                    currentNode = node
                    nextNode = node.next
                    newNode.next = nextNode
                    currentNode.next = newNode
                    break
                node = node.next
