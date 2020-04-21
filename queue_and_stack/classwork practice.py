# NOT PEP8
# Written by Riley Pence
# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, storage):  
        self.storage = storage  
        self.next = None 
class LinkedList: 
    def __init__(self): 
        self.head = None
    def push(self, new_storage): 
        new_node = Node(new_storage) 
        new_node.next = self.head 
        self.head = new_node 
    # Function to get the middle
    def printMiddle(self): 
        sl_scan = self.head 
        fst_scan = self.head 
        if self.head is not None: 
            while (fst_scan is not None and fst_scan.next is not None): 
                fst_scan = fst_scan.next.next
                sl_scan = sl_scan.next
            print("The middle element is: ", sl_scan.storage) 
list1 = LinkedList() 
list1.push(6)
list1.push(5) 
list1.push(23) 
list1.push(2) 
list1.push(3) 
list1.push(1)
list1.push(7) 
list1.printMiddle()

# def reverseOrder(head):
#   curr = head
#   prev = None
#   while curr.next is not None:
#     next = curr.next
#     curr.next = prev
#     prev = curr
#     curr = next
#   curr.next = prev
#   return curr.value

# hackerrank problem 
# count = 0

# current = head

# while count < 1002:
#     count += 1
#     if current.next != None:
#         current = current.next
#     else: 
#         return False
# return True 