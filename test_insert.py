from linked_list import linked_list, Node

from test_add import myList_0


#-----insert test-------
#-----1. insert at index----
myList_0.insert_at_index(929,2)
myList_0.display()
myList_0.insert_at_index(909,0)
myList_0.display()
myList_0.insert_at_index(9109,10)
myList_0.display()
myList_0.insert_at_index(9119,11)
myList_0.display()
myList_0.insert_at_index(999,9)
myList_0.display()
##-----2. insert before node-----
myList_0.insert_before_node(1,'y0')
myList_0.display()
myList_0.insert_before_node(1,'before1')
myList_0.display()
myList_0.insert_before_node(5,'before5')  # (cur_node.data not unique)
myList_0.display()
myList_0.insert_before_node(10,'before10')
myList_0.display()
myList_0.insert_before_node('x','new_x')
myList_0.display()
##-----3. insert after node-----
myList_0.insert_after_node(1,'after1')
myList_0.display()
myList_0.insert_after_node(4,'after4')
myList_0.display()
myList_0.insert_after_node(5,'after5')  # (cur_node.data not unique)
myList_0.display()
myList_0.insert_after_node(10,'after10')
myList_0.display()
myList_0.insert_after_node('x','new_x')
myList_0.display()