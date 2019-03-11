from linked_list_InterQ import Node, linked_list

# -----Interview Questions Testing-----
## Q3 - Delete Middle Node

# Input:  a -> b -> c -> d -> e -> f
# Output: a -> b -> d -> e -> f
myList_0 = linked_list()
myList_0.add('a')
myList_0.add('b')
myList_0.add('c')
myList_0.add('d')
myList_0.add('e')
myList_0.add('f')
myList_0.add('g')
myList_0.display()
myList_0.delete_middle_node()
myList_0.display()