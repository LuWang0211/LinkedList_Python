from linked_list_InterQ import Node, linked_list

# -----Interview Questions Testing-----
## Q4 - Partition
# Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 (partition = 5)
# Output 1: [3 -> 1 -> 2 -> 5 -> 5 -> 8 -> 10]
myList_0 = linked_list()
myList_0.add(3)
myList_0.add(5)
myList_0.add(8)
myList_0.add(5)
myList_0.add(10)
myList_0.add(2)
myList_0.add(1)
myList_0.add(6)
myList_0.add(7)
myList_0.display()
myList_0.partition(5)
myList_0.display()
myList_0.partition(6)
myList_0.display()