from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        # self.size = 0
        self.order = DoublyLinkedList()
        self.storage = {}

    #     MY WORK
    #     self.limit = limit
    #     self.storage = {}
    #     self.length = 0

    # def __str__(self):
    #     for key, value in self.storage.items():
    #         print('key', key)
    #         print('value', value)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

        ## CLASSWORK
        # # Key is not in cache 
        # if key not in self.storage:
        #     return None 

        # # Key is in cache
        # else: # We don't need the else statement because the compiler will see that the if is not true
        #     # move it to most recently used
        #     node = self.storage[key]
        #     self.order.move_to_end(node)
        #     # return value
        #     return node.value[1] # we return this since we store the value in a key value tuple





        # MY WORK
        # # Given a key, search storage for that key
        # # If key does not exist, return none
        # if key not in self.storage:
        #     return None
        # else: # if the key does exist in storage
        #     value = self.storage.get(key)
        #     # key needs to be moved to front
        #     # shift everything else to the back
        #     return value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    # self.storage = dict()
    # self.node = DoublyLinkedList()
    # self.storage[(key, value)] self.node.value
    # key = self.node.value
    # value = self.storage[key]

    def set(self, key, value):
        # key already exists
        if key in self.storage:
            # Overwrite the value
            node = self.storage[key]
            node.value = (key, value)
            # Move it to tail (most recently used)
            self.order.move_to_end(node)
            return 
        if len(self.order) == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()

        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
         
        ## CLASSWORK
        # # size is at limit
        # if len(self.order) == self.limit:
        #     # Remove the oldest one
        #     index_of_oldest = self.order.head.value[0]
        #     del self.storage[index_of_oldest]
        #     self.order.remove_from_head()

        #     # Add the new new one to the end
        #     self.order.add_to_tail((key, value))
        #     self.storage[key] = self.order.tail 

        # # size is not at limit
        # if len(self.order) < self.limit:
        #     # Add to order
        #     self.order.add_to_tail((key, value))
        #     # Add to storage
        #     self.storage[key] = self.order.tail 

        # # key already exists
        # if key in self.storage:
        #     # Overwrite the value
        #     node = self.storage[key]
        #     node.value = (key, value)
        #     # Move it to tail (most recently used)
        #     self.order.move_to_end(node)



        # MY WORK
        # if self.length == self.limit:
        #     # remove the last element
        #     self.length -= 1
        #     self.storage.pop(key)
        #     # shift all elements to the right
        #     self.length += 1
        #     self.storage.update({key: value})
        #     # insert new element at the front

        # else:
        #     self.length +=1
        #     new_node = DoublyLinkedList(value)
        #     self.storage.update({key: new_node})
        #     # shift all elements to the right
        #     # insert new element at the front


