from linked_list_InterQ import Node, linked_list

# -----Interview Questions Testing-----
# Q1 - Remove Dups(duplicates)

# Input:  2 -> 0 -> 5 -> 9 -> 5 -> 2 -> 0 -> 2 -> 1 
# Output: 2 -> 0 -> 5 -> 9 -> 1 
myList_0 = linked_list()
myList_0.add(2)
myList_0.add(0)
myList_0.add(5)
myList_0.add(9)
myList_0.add(5)
myList_0.add(2)
myList_0.add(0)
myList_0.add(2)
myList_0.add(1)
myList_0.display()

myList_0.remove_Dups()
myList_0.display()

myList_1 = linked_list()
myList_1.add(0)
myList_1.add(0)
myList_1.add(0)
myList_1.add(0)
myList_1.add(0)
myList_1.display()

myList_1.remove_Dups()
myList_1.display()

myList_2 = linked_list()
myList_2.add(0)
myList_2.add(1)
myList_2.add(2)
myList_2.add(3)
myList_2.add(4)
myList_2.display()

myList_2.remove_Dups()
myList_2.display()
