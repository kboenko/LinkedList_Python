import unittest
from entity import IteratedLinkedList as ill
from entity import Node as n

class ILLTest(unittest.TestCase):

    def test_next(self):
        iter_list = ill.IteratedLinkedList()

        iter_list.add_in_tail(n.Node(21))
        iter_list.add_in_tail(n.Node(58))
        iter_list.add_in_tail(n.Node(580))
        iter_list.add_in_tail(n.Node(582))

        a = next(iter_list)

        self.assertEqual(a.value, 58)

    def test_first(self):
        iter_list = ill.IteratedLinkedList()

        iter_list.add_in_tail(n.Node(21))
        iter_list.add_in_tail(n.Node(58))
        iter_list.add_in_tail(n.Node(580))

        next(iter_list)
        next(iter_list)
        a = next(iter_list)

        self.assertEqual(a.value, 21)

if __name__ == '__main__':
   unittest.main()