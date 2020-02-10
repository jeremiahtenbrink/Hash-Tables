# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return self._hash_djb2(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # Get the hashed key
        hash_key = self._hash_mod(key)

        # check if there is a LL in the array at the hash key index.
        if self.storage[hash_key] == None:
            # if no LL make one
            self.storage[hash_key] = LinkedPair(key, value)
        else:
            # Get the LL
            node = self.storage[hash_key]

            # check to see if key at the node is the same
            while node.next is not None and node.key != key:
                # if not the same go to next node
                node = node.next

            # check is the key is the same.
            if node.key == key:
                # set value = to the new value. overwrite the node
                node.value = value
            else:
                # create a new node for the key because it wasn't found
                node.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # get hash index
        hash_key = self._hash_mod(key)

        # get the LL at the given hash index
        node = self.storage[hash_key]

        # check if the node key is the same
        if node.key == key:
            # remove node by setting the LL head to the next node
            self.storage[hash_key] = node.next
        else:
            # search the LL for the key
            while node.next is not None and node.next.key != key:
                node = node.next

            # check if node.next key is the same.
            if node.next.key == key:
                # remove next node
                node.next = node.next.next
            else:
                print("The key was not found.")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get the hash index
        hash_key = self._hash_mod(key)

        # get the LL at the index
        node = self.storage[hash_key]

        # search the LL for the key
        while node is not None and node.next is not None and node.key != key:
            node = node.next

        # if the node key is the same return the value
        if node is not None and node.key == key:
            return node.value
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # copy the old storage
        old_storage = self.storage

        # double capacity
        self.capacity = self.capacity * 2

        # create new storage
        self.storage = [None] * self.capacity

        # loop through old storage inserting items one by one in to new storage
        for i in range(len(old_storage)):
            node = old_storage[i]
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
