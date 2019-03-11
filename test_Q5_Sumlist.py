from linked_list_InterQ import Node, linked_list

# -----Interview Questions Testing-----
## Q5 - Sum_list
# reverse order
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2)
# Output: 2  -> 1  -> 9
print('Reverse order :List 1 + List 2')
List_1 = linked_list()
List_1.add(7)
List_1.add(1)
List_1.add(6)
List_1.display()
List_2 = linked_list()
List_2.add(5)
List_2.add(9)
List_2.add(2)
List_2.add(9)
List_2.display()
print('Reverse order result:')
myList_0 = linked_list.sum_lists(List_1, List_2)
myList_0.display()

# forward order
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5)
# Output: 9  -> 1  -> 2
print('Forward order :List 1 + List 2')
List_1 = linked_list()
List_1.add(6)
List_1.add(1)
List_1.add(7)
List_1.display()
List_2 = linked_list()
List_2.add(2)
List_2.add(9)
# List_2.add(5)
List_2.display()
print('Forward order result:')
myList_0 = linked_list.sum_lists(List_1, List_2, 'Forward')
myList_0.display()