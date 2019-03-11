from linked_list import linked_list, Node

#test
# Runner Technique test 
# a0 -> a1 -> a2 -> b0 -> b1 -> b2
# a0 -> b0 -> a1 -> b1 -> a2 -> b2
# List_0 = Linked_list()
# List_0.add('a0')
# List_0.add('a1')
# List_0.add('a2')
# List_0.add('b0')
# List_0.add('b1')
# List_0.add('b2')
# List_0.display()
# List_0.runner_sorted()
# List_0.display()

# bubble_sort test
# 5 -> 3 -> 1 -> 6 -> 7 -> 2 -> 8 -> 4
# 1st swap: 3 -> 1 -> 5 -> 6 -> 2 -> 7 -> 4 -> 8
# result:   1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
List_1 = linked_list()
List_1.add(5)
List_1.add(3)
List_1.add(1)
List_1.add(6)
List_1.add(7)
List_1.add(2)
List_1.add(8)
List_1.add(4)
List_1.display()
#List_1.bubble_sort_1()
List_1.bubble_sort_2()
List_1.display()

List_2 = linked_list()
List_2.add(8)
List_2.add(3)
List_2.add(5)
List_2.add(6)
List_2.add(7)
List_2.add(2)
List_2.add(4)
List_2.add(1)
List_2.display()
#List_2.bubble_sort_1()
List_2.bubble_sort_2()
List_2.display()

