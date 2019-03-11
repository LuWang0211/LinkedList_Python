from linked_list_InterQ import Node, linked_list, Circular_Linked_List

# -----Interview Questions Testing-----
## Q8 - Loop Detection
myList_0 = Circular_Linked_List()
myList_0.add('a')
myList_0.add('b')
myList_0.add('c')
myList_0.add('d')
myList_0.display()
print(myList_0.length())
list_circularpart = Circular_Linked_List()
list_circularpart.add(1)
list_circularpart.add(2)
list_circularpart.add(3)
list_circularpart.display()
print(list_circularpart.length())

## connect two lists
head_1 = myList_0.root
head_2 = list_circularpart.root
while head_1:
    if head_1.next == myList_0.root:
        head_1.next = head_2
        break
    head_1 = head_1.next

head_1 = myList_0.root
total = 0

## print out the list
while head_1:
    if head_1 == head_2:
        total += 1
    if total == 2:
        print(f'print stop- back to loop detection:{head_1}')
        break
    print(f'print list nodes:{head_1}')
    head_1 = head_1.next

## find the node
print(f'Result- find Loop Detection:{myList_0.loop_detection()}')