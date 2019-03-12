class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f'({self.data})'

class linked_list:
    def __init__(self):
        self.head = None

    # Add a new node with 'data'
    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node

    # Count linked_list length
    def length(self):
        cur = self.head
        total = 0
        
        while cur: 
            total += 1           
            cur = cur.next

        return total

    # Print out in list form
    def display(self):
        data_elems = []
        cur_node = self.head
        while cur_node != None:
            #print(f'---:{cur_node.data}')
            data_elems.append(cur_node.data)
            cur_node = cur_node.next
        print(data_elems)

    #staticmethod: From a list to linkedlist(instead add() individuly)
    @staticmethod
    def from_list(origin_list):
        linkedlist = linked_list()
        if len(origin_list) == 0:
            print('Error: The list is None, can change to linked list!')
            linkedlist.head = None
        else:
            linkedlist.head = Node(origin_list[0])
            cur_node = linkedlist.head

        for i in range(1, len(origin_list)):
                cur_node.next = Node(origin_list[i])
                cur_node = cur_node.next

        return linkedlist

    #classmethod: From a list to linkedlist(instead add() individuly)
    @classmethod
    def from_list_cls(cls, origin_list):
        linkedlist = cls()
        if len(origin_list) == 0:
            print('Error: The list is None, can change to linked list!')
            linkedlist.head = None
        else:
            linkedlist.head = Node(origin_list[0])
            cur_node = linkedlist.head

        for i in range(1, len(origin_list)):
                cur_node.next = Node(origin_list[i])
                cur_node = cur_node.next

        return linkedlist

    ##---------------Interview Questions---------------
    ## Q1 - Remove Dups(duplicates)
    def remove_Dups(self):
        cur_node = self.head
        per_node = None

        Dups_value = dict()   # record unique node.data
        linked_list_size = 0  # record list node.data numbers

        if cur_node is None or cur_node.next is None:
            print('Warning: This linked list is None or only includes one node. No Duplicates!')
            return

        while cur_node:
            if cur_node.data not in Dups_value: # a node.data shows at first time
                Dups_value[cur_node.data] = True
                per_node = cur_node
            else:                               # remove node
                per_node.next = cur_node.next

            cur_node = cur_node.next            # move to next node
            linked_list_size += 1               
        
        if len(Dups_value) == linked_list_size: # determine whether the list includes duplicates
            print('No duplicates!! Retrun the same linked_list')
            return

    ## Q2 - Return Kth to Last  ## find a node in reverse order
    ## Method 1: fint the node index in ascending order by counting the list length
    def Return_Kth_to_Last_method1(self, k):
        cur_node = self.head
        list_length = self.length()

        if k >= list_length or k < 0: 
            print(f'Error: {k} is out of the list range!')

        node_index = list_length - k - 1  # find index of the node in ascending order
        index_count = 0
        while cur_node:                   # find the node
            if index_count == node_index:
                return cur_node
            index_count += 1
            cur_node = cur_node.next
    
    ## Method 2: two pointer, the fast_node index = cur_node index + k
    def Return_Kth_to_Last_method2(self, k):
        cur_node = self.head
        fast_node = self.head

        if k < 0 or self.head is None: 
            print(f'Error: {k} is out of the list range!')

        count = 0
        while fast_node and count < k:      # move fast_node to kth position from cur_node(self.head)
            fast_node = fast_node.next
            count += 1

        if fast_node is None and count < k: # when do not know the length, check if the k out of list range
            print(f'Error: {k} is out of the list range!')
            return None

        while cur_node and fast_node:       # move cur_node and fast_node simultaneously, each time 1 step 
            if fast_node.next is None:
                return cur_node
            fast_node = fast_node.next
            cur_node = cur_node.next
    
    ## Q3 - Delete Middle Node
    def delete_middle_node(self):
        fast_node = self.head
        cur_node  = self.head

        if self.head is None or self.head.next is None:
            print('Error: This linked list is None or only includes one node. No Middle Node!')
            return self
        if self.head.next.next is None:
            print('Warning: The list only includes two nodes. If Implement, the first node will be deleted!')
            implement_request = input('Do you want to do this? (N/Y) ')    
            if implement_request == 'Y':
                self.head = self.head.next
                return self
            elif implement_request == 'N':
                return self
        
        while fast_node and cur_node:
            per_cur_node = cur_node
            fast_node = fast_node.next.next
            cur_node = cur_node.next

            if fast_node.next is None or fast_node.next.next is None:
                per_cur_node.next = cur_node.next
                cur_node.next = None
                break

    ## Q4 - Partition
    def partition(self, data):

        if self.head is None or self.head.next is None:
            print('Error: This linked list length is to short(less than 2). Can not be partition!')
            return self

        swap_num = None
        while swap_num != 0 :              # loop until no nodes need to be swap
            swap_num = 0
            per_node = self.head
            cur_node = per_node.next

            # Compare adjacent nodes between the partition data
            # move less data to left side, and larger data to right side
            while cur_node:
                if (per_node.data >= data and cur_node.data < data) or (per_node.data > data and cur_node.data <= data):
                    temp_data = per_node.data
                    per_node.data = cur_node.data
                    cur_node.data = temp_data
                    swap_num += 1           # record swap times in each loop
                per_node = cur_node         # adjacent nodes do not need to swap, then keep move
                cur_node = cur_node.next


    ## Additional function
    ## Reverse list function : Q5, Q6 will use this function (Q6 method 2 do not need this function)
    def reverse(self):
        per_node = None 
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = per_node

            per_node = cur_node 
            cur_node = next_node 
        self.head = per_node

    ## Q5 - Sum List
    ## Sum List function
    @staticmethod
    def sum_lists(list1, list2, order='Reverse'):

        if list1.head is None and list2.head is None:
            print('Error: the two numbers both is None!')

        list1_length = list1.length() 
        list2_length = list2.length()

        max_length = max(list1_length, list2_length) # count digit will be add times

        l1 = list1.head
        l2 = list2.head
        sum_list = linked_list()

        # lopp digits
        while max_length != 0: 
            # add each digit, the list with less length, empty digit = 0
            # (7 -> 1 -> 6) + ( 5 -> 9 )
            # sum_list = (7 + 5  -> 1 + 9  -> 6 + 0)                      
            if l1 is None and l2 is not None:
                l1_data = 0
                l2_data = l2.data
                l2 = l2.next
            elif l2 is None and l1 is not None:
                l1_data = l1.data
                l1 = l1.next
                l2_data = 0
            else:
                l1_data = l1.data
                l2_data = l2.data
                l1 = l1.next
                l2 = l2.next
            # print(l1_data, l2_data)

            if l1_data >= 10 or l2_data >= 10:
                print('Input Error: Node contains more than a digit. Can not calculate!')
                break

            sum_data = l1_data + l2_data
            sum_list.add(sum_data)
            # print(sum_data )
            max_length -= 1

        # Forward order, result reverse
        # (6 -> 1 -> 7) + ( 2 -> 9 )
        # sum_list = (6 + 2  -> 1 + 9  -> 7 + 0)
        # sum_list = (7      -> 10     -> 8) 
        if order == 'Forward':
            sum_list.reverse()
        
        # sum_list calculate to each digit in [0, 9]
        # sum_list = (12  -> 10  -> 6) 
        # sum_list = (2(carry=1)  -> 1(carry1)  -> 7(carry=0)) 
        carry = 0
        sum_cur_node = sum_list.head
        while sum_cur_node:
            if sum_cur_node.data >= 10:
                sum_cur_node.data = sum_cur_node.data + carry - 10
                carry = 1
            else:
                sum_cur_node.data = sum_cur_node.data + carry
                carry = 0
                if sum_cur_node.data >= 10:
                    sum_cur_node.data = sum_cur_node.data - 10
                    carry = 1

            sum_cur_node = sum_cur_node.next
        
            if sum_cur_node is None and carry == 1:
                sum_list.add(1)

        # Forward order, result reverse
        if order == 'Forward':
            sum_list.reverse()

        return sum_list

    ## Q6 - Palindrome
    def palindrome_check(self):
        if self.head is None:
            print('Error: This list is None!')
            return False

        # Method 1: compare with a new linked list
        # Method 2: compare with a list
        '''
        # Method 1
        # Do not change the list: make a copy of list data, reverse new link list 
        #---------------------
        cur_node = self.head                  # make a data copy of list, and reverse new list
        reverse_list = linked_list()

        while cur_node:                        
            reverse_list.add(cur_node.data)
            cur_node = cur_node.next
        
        reverse_list.reverse()

        cur_node = self.head                   # compare two linked list
        reverse_list_node = reverse_list.head

        check_flag = True
        while cur_node and reverse_list_node:
            # print(cur_node.data ,reverse_list_node.data)
            if cur_node.data != reverse_list_node.data:
                check_flag = False
                break
            check_flag = True
            cur_node = cur_node.next
            reverse_list_node = reverse_list_node.next
        #---------------------
        '''
        
        # Method 2 : make a list , not a  linked list
        cur_node = self.head                  # make a data copy of list, and reverse new list
        datalist = list()
        count = 0
        while cur_node:                        
            datalist.append(cur_node.data)
            count += 1
            cur_node = cur_node.next        

        cur_node = self.head                  # list reverse loop (from end to head), compare to linked list
        check_flag = True
        for i in range(count-1, 0, -1):
            # print(f'datalist[{i}] = {datalist[i]}', f'cur_node = {cur_node.data}')
            if datalist[i] != cur_node.data:
                check_flag = False
                break
            check_flag = True
            cur_node = cur_node.next
        #---------------------      

        if check_flag:
            print('Yes! It is a palindrome!')
            return True
        else:
            print('No! It is not a palindrome!')
            return False

    ## Q7 - Intersection
    @staticmethod
    def Intersection(list1, list2):
        l1 = list1.head
        l2 = list2.head
        if list1.head is None or list2.head is None:
            print('Error: One or Both lists is None! No intersection!')
            return False
        
        # make a node_dic to determine if there is same nodes in two linked lists
        node_dic = dict()

        count = 0
        while l1:               # save all nodes in list1 into dict
            node_dic[l1] = count
            l1 = l1.next
            count +=1
        
        while l2:               # loop list 2, if node in dict -> intersection
            if l2 in node_dic:
                print(f'Intersection: {l2} is the intersectiog node!')
                return l2
            l2 = l2.next
        print(f'No Intersection: there is not a intersectiog node!')


## Q8 - Circular_Linked_List : loop detection
class Circular_Linked_List:
    def __init__(self, root=None):
        self.root = root

    # Add a new node with 'data'
    def add(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            new_node.next = self.root
        else:
            cur_node = self.root
            while cur_node.next != self.root:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.root

            # print(cur_node)
            # print(cur_node.next)

    # Count linked_list length
    def length(self):
        root_node = self.root
        cur_node  = self.root
        total = 0
        if self.root is None:
            print('Circular_Linked_List is None!')
            return False
        if cur_node.next == self.root:
            total += 1
        while cur_node.next != root_node: 
            total += 1           
            cur_node = cur_node.next
            if cur_node.next == root_node:
                total += 1
        return total

    # Print out in list form
    def display(self):
        data_elems = []
        cur_node = self.root
        if cur_node is None:
            print('Circular_Linked_List is None!')
            return False

        if cur_node.next == self.root:
            data_elems.append(cur_node.data)
            cur_node = cur_node.next
        while cur_node.next != self.root:
            data_elems.append(cur_node.data)
            cur_node = cur_node.next
            if cur_node.next == self.root:
                data_elems.append(cur_node.data)

        print(data_elems)  

    ## Q8 - Circular_Linked_List : loop detection
    def loop_detection(self):
        cur_node = self.root
        node_dict = dict()
        count = 0
        while cur_node:
            if cur_node not in node_dict:
                node_dict[cur_node] = count
            else:
                return cur_node
            cur_node = cur_node.next
            count += 1
            