from linked_list import linked_list, Node

from test_add import myList_0

#-----remove test-------
myList_0.remove_middle_node()
myList_0.display()

# Remove a node with 'data' by node
node = myList_0.get(2)
print(f"the dongxi: {node}")
myList_0.remove(node)
myList_0.display()

# removeByValue
myList_0.removeByValue(7)
myList_0.display()
print(myList_0.length())

# remove the Kth node
myList_0.remove_Kth(1)
myList_0.display()

myList_0.remove_Kth(1)
myList_0.display()