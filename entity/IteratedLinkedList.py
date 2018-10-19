from entity import LinkedList as ll
from exceptions import StopIterationException as si_ex

class IteratedLinkedList(ll.LinkedList):

    def __init__(self):
        super(IteratedLinkedList, self).__init__()
        self.current = None

    def __next__(self):
        try:
            if self.current.next is None:
                raise si_ex.StopIterationException('The end of list is reached!')
            self.current = self.current.next
        except si_ex.StopIterationException as e:
            #self.__first__()
            print('The end of list is reached!')

        return self.current

    def add_in_tail(self, node):
        if self.head is None:
            self.head = node
            self.current = self.head
        else:
            self.tail.next = node

        self.tail = node

    def first(self):
        self.current = self.head