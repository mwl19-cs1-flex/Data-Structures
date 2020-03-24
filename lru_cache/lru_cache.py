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
        self.storage = {}
        self.length = 0

    def __str__(self):
        for key, value in self.storage.items():
            print('key', key)
            print('value', value)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Given a key, search storage for that key
        # If key does not exist, return none
        if key not in self.storage:
            return None
        else: # if the key does exist in storage
            value = self.storage.get(key)
            # key needs to be moved to front
            # shift everything else to the back
            return value

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
    def set(self, key, value):
        if self.length == self.limit:
            # remove the last element
            self.storage.pop()
            # shift all elements to the right
            self.storage.update({key: value})
            # insert new element at the front

        else:
            self.length +=1
            new_node = DoublyLinkedList(value)
            new_node.next = new_node.prev 
            self.storage.update({key: value})
            # shift all elements to the right
            # insert new element at the front

test_cache = LRUCache(3)
test_cache.set('1', 'apple')
test_cache.set('2', 'banana')
test_cache.set('3', 'pear')
test_cache.set('4', 'orange')
print(test_cache)
