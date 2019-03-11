from linked_list_InterQ import Node, linked_list

# -----Interview Questions Testing-----
## Q2 - Return Kth_to_Last
# Linke:  a -> b -> c -> d -> e -> f
# Input:  k = 0 , Output:  (f)
# Input:  k = 2 , Output:  (d)
# Input:  k = 4 , Output:  (b)

myList_0 = linked_list()
myList_0.add('a')
myList_0.add('b')
myList_0.add('c')
myList_0.add('d')
myList_0.add('e')
myList_0.add('f')
myList_0.display()

print(f'method 1: 0th to last one is {myList_0.Return_Kth_to_Last_method1(0)}')
print(f'method 1: 2th to last one is {myList_0.Return_Kth_to_Last_method1(2)}')
print(f'method 1: 4th to last one is {myList_0.Return_Kth_to_Last_method1(4)}')

print(f'method 2: 0th to last one is {myList_0.Return_Kth_to_Last_method2(0)}')
print(f'method 2: 2th to last one is {myList_0.Return_Kth_to_Last_method2(2)}')
print(f'method 2: 4th to last one is {myList_0.Return_Kth_to_Last_method2(4)}')
