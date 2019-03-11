from linked_list_InterQ import Node, linked_list

# -----Interview Questions Testing-----
## Q6 - palindrome_check
# Input: a b b a
# Output: True
myList_0 = linked_list()
myList_0.add('a')
myList_0.add('b')
myList_0.add('b')
myList_0.add('a')
myList_0.display()
myList_0.palindrome_check()
myList_0.display()