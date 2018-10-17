from entity import LinkedList as ll
from entity import Node as n

node1 = n.Node(3)
node2 = n.Node(58)

list = ll.LinkedList()

list.add_in_tail(node1)
list.add_in_tail(node2)
list.add_in_tail(node2)
list.add_in_tail(n.Node(21))
list.add_in_tail(n.Node(58))

print(str(list.get_length()))