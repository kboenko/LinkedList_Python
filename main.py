from entity import LinkedList as ll
from entity import IteratedLinkedList as ill
from entity import Node as n

node1 = n.Node(3)
node2 = n.Node(58)

list = ll.LinkedList()

list.add_in_tail(node1)
list.add_in_tail(node2)
list.add_in_tail(node2)
list.add_in_tail(n.Node(21))
list.add_in_tail(n.Node(58))

# print(str(list.get_length()))

iter_list = ill.IteratedLinkedList()

iter_list.add_in_tail(n.Node(21))
iter_list.add_in_tail(n.Node(58))
iter_list.add_in_tail(n.Node(580))
iter_list.add_in_tail(n.Node(582))

print(iter_list.current)
print(iter_list.head)
# print(iter_list.tail)
# print (iter_list.get_values())

print('____________________________________________')

arr = []

print(iter_list.current)

arr.append(iter_list.__next__())
arr.append(iter_list.__next__())
arr.append(iter_list.__next__())
arr.append(iter_list.__next__())
arr.append(iter_list.__next__())
# print(iter_list.__next__())
# print(iter_list.__next__())

arr_val = []

for i in arr:
    arr_val.append(i.value)

print(arr_val)