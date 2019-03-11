from linked_list import linked_list, Node

from test_add import myList_0

#-----remove test-------
myList_0.remove_middle_node()
myList_0.display()

node = myList_0.get(2)
print(f"the dongxi: {node}")
myList_0.remove(node)
myList_0.display()

myList_0.remove(7)
myList_0.display()
print(myList_0.length())