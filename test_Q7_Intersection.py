from linked_list_InterQ import Node, linked_list
#from linked_list import Node, linked_list # use get()

# -----Interview Questions Testing-----
## Q7 - Intersection
# List1: 1 -> 2 -> 3 -> 4 ->
# same part:              -> 9 -> 10 -> 11
# List2:           7 -> 8 ->
# the node is (9)
print('before intersection:')
myList_1 = linked_list()
myList_1.add(1)
myList_1.add(2)
myList_1.add(3)
myList_1.add(4)
myList_1.display()
myList_2 = linked_list()
myList_2.add(7)
myList_2.add(8)
myList_2.display()

## '''
myList_Intersection = linked_list()
myList_Intersection.add(9)
myList_Intersection.add(10)
myList_Intersection.add(11)
myList_Intersection.display()

myList_1_cur = myList_1.head
myList_2_cur = myList_2.head
myList_Intersection_cur = myList_Intersection.head
print(f'intersectiong node: {myList_Intersection_cur}')

while myList_1_cur:
    myList_1_cur = myList_1_cur.next
    if myList_1_cur.next is None:
        myList_1_cur.next = myList_Intersection_cur
        break
while myList_2_cur:
    myList_2_cur = myList_2_cur.next
    if myList_2_cur.next is None:
        myList_2_cur.next = myList_Intersection_cur
        break
##'''

print('after intersection:')
myList_1.display()
myList_2.display()
# print(myList_1.get(4)) # import linked_listtest if successfully create instance 
# print(myList_2.get(2))

# if myList_1.get(4) == myList_2.get(2):
#     print('Create Done!')
print('intersection check result:')
myList_0 = linked_list.Intersection(myList_1, myList_2)