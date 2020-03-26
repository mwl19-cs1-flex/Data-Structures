import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if new < node.value
        if value < self.value:
            # if left doesnt exist
            if self.left is None:
                # create left
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
        # if value >= self.value: can do this
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    #     MY WORK (PASSES TESTS)
    #     if value < self.value and self.left == None:
    #         self.left = BinarySearchTree(value)
    #         # self.value.left.insert(value)
    #         # self.left = BinarySearchTree(value)
    #     elif value >= self.value and self.right == None:
    #         self.right = BinarySearchTree(value)
    #         # self.value.right.insert(value)
    #         # self.right = BinarySearchTree(value)
    #     elif value < self.value and self.left != None:
    #         self.left.insert(value)
    #     elif value >= self.value and self.right != None:
    #         self.right.insert(value)

    
    # # Return True if the tree contains the value
    # # False if it does not
    def contains(self, target):
    # WHY DO WE NEED RETURN?!
    # We need a return because we have a return in our base case
    # To get that base case from our recursion, we need to return the results of that recursion
    # We need a return because we're finding something, not doing something
        if target == self.value:
            return True 
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        if target >= self.value:
            if self.right is None:
                return False
            else: 
                return self.right.contains(target)




        # MY WORK (PASSES TESTS)
        # if target == self.value:
        #     return True
        # else:
        #     if target < self.value and self.left == None:
        #         return False
        #     elif target >= self.value and self.right == None:
        #         return False
        #     elif target < self.value and self.left != None:
        #         return self.left.contains(target)
        #     elif target >= self.value and self.left != None:
        #         return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if there's a right:
        # get max on right
        # else
        # return node value

        # We need a return because we have a return in our base case
        # To get that base case from our recursion, we need to return the results of that recursion
        # We need a return because we're finding something, not doing something
        if self.right:
            return self.right.get_max()
        else:
            return self.value

        # MY WORK (PASSES TESTS)
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
        cb(self.value)
        # Want to address both sides that's why we use if and not elif



    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
