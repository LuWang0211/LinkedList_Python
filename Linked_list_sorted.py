## Linked_list_sorted
## method 1: Runner Technique - a sorted linked list
## method 2: Bubble sort - a sorted linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"({self.data})"

class Linked_list:
    def __init__(self):
        self.head = None

    # Adds new node with 'data'
    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node

    # Prints out in list form. 
    def display(self):
        data_elems = []
        cur_node = self.head
        while cur_node != None:
            #print(f'---:{cur_node.data}')
            data_elems.append(cur_node.data)
            cur_node = cur_node.next
        print(data_elems)
    
    # Runner Technique -  - a sorted linked list
    def runner_sorted(self):
        cur_node_1 = self.head
        cur_node_2 = self.head
        # index_1 = 0
        # index_2 = 0

        if self.head is None or self.head.next is None:
            print('Error: The list is None or only includes one node,can not be sorted')
            return self

        if cur_node_2.next.next is None:
            print('Warning: The list only includes two nodes, sorted result equal to the original list')
            return self
        
        while cur_node_1 and cur_node_2:
            # print(f'{index_1}:{cur_node_1}', f'{index_2}:{cur_node_2}')
            cur_node_1 = cur_node_1.next.next
            cur_node_2 = cur_node_2.next
            # index_1 += 2
            # index_2 += 1
            # print(f'after moved: {index_1}:{cur_node_1}', f'{index_2}:{cur_node_2}')

            if cur_node_1.next is None or cur_node_1.next.next is None:
                cur_node_1 = self.head
                per_cur_node_2 = cur_node_2
                cur_node_2 = cur_node_2.next
                per_cur_node_2.next = None
                # index_1 == 0
                # index_2 += 1
                print(f'after loop: {cur_node_1}', f'{cur_node_2}')
                break
        # print(f'after loop: {index_1}:{cur_node_1}', f'{per_cur_node_2}', f'{index_2}:{cur_node_2}')
        while cur_node_2:
            # copy cur_node_2(b0) and remove from list 
            # # a0 -> a1 -> a2 -> b1 -> b2 , temp_node = b0
            temp_node = cur_node_2
        #    per_cur_node_2.next = cur_node_2.next
        #    cur_node_2 = per_cur_node_2.next
            cur_node_2 = cur_node_2.next
            print(f'after loop: {cur_node_1}', f'{cur_node_2}')

            # insert the copy of cur_node_2(b0) and remove between cur_node_1(a0) and cur_node_1(a1)
            #print(f'befor insert: cur_node_1={cur_node_1}', f'cur_node_2 = {cur_node_2}',f'a2.next = {per_cur_node_2.next}',f'temp_node = {temp_node}')
            temp_node.next = cur_node_1.next
            cur_node_1.next = temp_node
            cur_node_1 = temp_node.next
            print(f'after loop: {cur_node_1}', f'{cur_node_2}')
            #print(f'after insert: temp_node = {temp_node}', f'temp_node.next = {temp_node.next}', f'cur_node_1={cur_node_1}', f'cur_node_1.next={cur_node_1.next}')
            #break
    # Bubble sort(method 1) -  - a sorted linked list
    def bubble_sort_1(self):

        if self.head is None or self.head.next is None:
            print('Error: The list is None or only includes one node,can not be sorted')
            return self

        per_node = self.head
        cur_node = per_node.next

        temp_data = None
        max_node  = None

        index = 0
        fist_loop_flag = True
        while index != 1:
            while True:
                #print(f'!!-----------:per_node={per_node}',f'per_node.next={per_node.next}',f'cur_node={cur_node}',f'cur_node.next={cur_node.next}')
                if per_node.data >= cur_node.data:
                    temp_data = per_node.data
                    per_node.data = cur_node.data
                    cur_node.data = temp_data
                #print(f'!!change data:per_node={per_node}',f'per_node.next={per_node.next}',f'cur_node={cur_node}',f'cur_node.next={cur_node.next}')

                if cur_node.next is None or cur_node.next == max_node:
                    fist_loop_flag = False
                    max_node = cur_node
                    if cur_node.next is None:
                        index +=1
                    else:
                        index -=1
                    #print(f'loop2--{index}th : max_node={max_node}')
                    #print(index)
                    per_node = self.head
                    cur_node = per_node.next
                    #print(f'!move to next:per_node={per_node}',f'per_node.next={per_node.next}',f'cur_node={cur_node}',f'cur_node.next={cur_node.next}')
                    #self.display()
                    if index == 1 :
                        if per_node.data >= cur_node.data:
                            temp_data = per_node.data
                            per_node.data = cur_node.data
                            cur_node.data = temp_data             
                    break
                
                per_node = cur_node
                cur_node = cur_node.next
                if fist_loop_flag:
                    index += 1
                #print(index)
                #print(f'!move to next:per_node={per_node}',f'per_node.next={per_node.next}',f'cur_node={cur_node}',f'cur_node.next={cur_node.next}')
    
    # Bubble sort(method 2) -  - a sorted linked list
    # linked_list size
    def length(self):
        cur = self.head
        total = 0
        
        while cur : 
            total += 1           
            cur = cur.next

        return total
    
    def bubble_sort_2(self):
        if self.head is None or self.head.next is None:
            print('Error: The list is None or only includes one node,can not be sorted')
            return self

        list_length = self.length()

        for max in range(list_length - 1, 0, -1):
            per_node = self.head
            cur_node = per_node.next
            i = 0

            while i < max:
                if per_node.data >= cur_node.data:
                    temp_data = per_node.data
                    per_node.data = cur_node.data
                    cur_node.data = temp_data
                
                per_node = cur_node
                cur_node = cur_node.next
                i += 1

            