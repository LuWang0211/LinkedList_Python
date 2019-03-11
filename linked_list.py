class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"({self.data})"

class linked_list:
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

    # linked_list size
    def length(self):
        cur = self.head
        total = 0
        
        while cur : 
            total += 1           
            cur = cur.next

        return total

    # Prints out in list form. 
    def display(self):
        data_elems = []
        cur_node = self.head
        while cur_node != None:
            #print(f'---:{cur_node.data}')
            data_elems.append(cur_node.data)
            cur_node = cur_node.next
        print(data_elems)
    
    # Returns the value of the node at 'index'. 
    def get(self, index):
        if index < 0: # no data
            print(f"ERROR: 'Get' Index({index}) out of range!")
            return None
        
        cur_idx = 0
        cur_node = self.head
        if cur_node is None:
            print(f"ERROR: 'Get' Index({index}) out of range!")
            return None
        while cur_node is not None:
            if cur_idx == index:
                return cur_node

            cur_node = cur_node.next            
            cur_idx += 1
            if cur_node is None and cur_idx <= index:
                print(f"ERROR: 'Get' Index({index}) out of range!")
                return None

    # Remove a node with 'data' by node
    def remove(self, node):
        this_node = self.head
        prev_node = None
        
        while this_node:
            if this_node == node:
                if prev_node:
                    prev_node.next = this_node.next
                else:
                    self.head = this_node.next
                #self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.next
        return False  # data not found

    # Remove a node with 'data' by data
    def removeByValue(self, data):
        curNode = self.head
        prevNode = None

        while curNode:
            curData = curNode.data

            if curData == data:
                # remove current node
                if not prevNode:
                    self.head = curNode.next
                else:
                    prevNode.next = curNode.next

            prevNode = curNode
            curNode = curNode.next
    
    
    # delete middle node
    def remove_middle_node(self):
        listsize = self.length()
        if listsize % 2 == 0:
            index = listsize / 2 - 1
        else:
            index = (listsize - 1) / 2 
        middle_node = self.get(index)
        self.remove(middle_node)

    # insert a node with 'data' at 'index'
    def insert_at_index(self, data, index):
        cur_node = self.head
        prev_node = self.head
        cur_node_idx = 0

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        if cur_node is None and index != 0:
            print(f"ERROR: Index({index}) out of range!")
            return None           

        while True:
            cur_node = cur_node.next
            if cur_node_idx+1 == index: 
                new_node = Node(data)
                prev_node.next = new_node
                new_node.next = cur_node
                return
            prev_node = cur_node
            cur_node_idx +=1
            if cur_node is None and cur_node_idx <= index:
                print(f"ERROR: Index({index}) out of range!")
                return None
    
    # insert a node with 'data' before the cur_node with 'data_1'
    def insert_before_node(self, cur_node_data, data):
        new_node = Node(data)
        pre_node = self.head
        flag = 0

        if self.get(0).data == cur_node_data:
            new_node.next = self.head
            self.head = new_node
            flag = 1

        cur_node = pre_node.next
    
        while cur_node is not None:
            if cur_node.data == cur_node_data:
                new_new_node = Node(data)
                new_new_node.next = cur_node
                pre_node.next = new_new_node
                flag = 1

            cur_node = cur_node.next
            pre_node = pre_node.next

        if flag == 0:
            print('this node is not in list,can not insert data before it')
            return None

    # insert a node with 'data' after the cur_node with 'data_1'
    def insert_after_node(self, cur_node_data, data):
        cur_node = self.head
        new_node = Node(data)
        flag = 0
        
        while cur_node:
            #print(f'1:{cur_node}')
            if cur_node.data == cur_node_data:
                if flag == 0:
                    new_node.next = cur_node.next
                    cur_node.next = new_node
                    flag = 1
                else:
                    new_new_node = Node(data)
                    new_new_node.next = cur_node.next
                    cur_node.next = new_new_node
            cur_node = cur_node.next
            #print(f'2:{cur_node}')
        if flag == 0:
            print('this node is not in list,can not insert data after it')
            return None


    #merge two linked list- change lists
    def merge_sorted(self, llist):
        list1 = self.head 
        list2 = llist.head
        s = None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1 and list2:
            if list1.data <= list2.data:
                s = list1 
                list1 = s.next
            else:
                s = list2
                list2 = s.next
            new_head = s 
        while list1 and list2:
            if list1.data <= list2.data:
                s.next = list1 
                s = list1 
                list1 = s.next
            else:
                s.next = list2
                s = list2
                list2 = s.next
        if not list1:
            s.next = list2 
        if not list2:
            s.next = list1 
        return new_head

    #merge two linked list- creat a new list
    @staticmethod
    def merge(list1, list2):
        l1 = list1.head
        l2 = list2.head
        mergedlist = linked_list()
        cur_node = mergedlist.head

        if l1 is None:
            return list2
        if l2 is None:
            return list1

        while l1 and l2:
            if l1.data <= l2.data:
                new_data = l1.data
                l1 = l1.next
            else:
                new_data = l2.data
                l2 = l2.next
            new_node = Node(new_data)
            if cur_node is None:
                mergedlist.head = new_node
            else:
                cur_node.next = new_node
            cur_node = new_node
        
        while l1 is not None:
            new_data = l1.data
            l1 = l1.next
            new_node = Node(new_data)
            cur_node.next = new_node
            cur_node = new_node
            
        while l2 is not None:
            new_data = l2.data
            l2 = l2.next
            new_node = Node(new_data)
            cur_node.next = new_node
            cur_node = new_node

        return mergedlist

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
    # linked_list size- use def length()
    #    
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

            