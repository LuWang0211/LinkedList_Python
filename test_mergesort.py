from linked_list import linked_list, Node #, merge

#-----merge_sorted test-------
# # myList_1 : 1 5 7 9 10
# # myList_2 : 2 3 4 6 8
myList_1 = linked_list()
myList_2 = linked_list()

myList_1.add(1)
myList_1.add(5)
myList_1.add(7)
myList_1.add(9)
myList_1.add(10)
# myList_1.add(11)
myList_1.display()

myList_2.add(2)
myList_2.add(3)
myList_2.add(4)
myList_2.add(6)
myList_2.add(8)
myList_2.add(12)
myList_2.display()

#-----1. merge_sorted() test---(change list 1, 2)-------
# # myresult (myList_1): 1 2 3 4 5 6 7 8 9 10
# myList_1.merge_sorted(myList_2)
# print('after merge_sorted() list 1:') #
# myList_1.display()
# print('after merge_sorted() list 2:') #wenti
# myList_2.display()

#-----2. merge_sorted() test---(do not change list 1, 2)-------
# # myresult : 1 2 3 4 5 6 7 8 9 10
#myresult = linked_list()
myresult = linked_list.merge(myList_1, myList_2)
#myresult.merge(myList_1, myList_2)
# print('after merged list 1:') #
# myList_1.display()
# print('after merged list 2:') 
# myList_2.display()
print('after merged result:')
myresult.display()
