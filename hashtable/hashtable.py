class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self, head):
        self.head = head


class HashTable:

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.size = 0
        self.head = None
        # self.hash = [None] * self.capacity
        self.hash = [LinkedList(self.head)] * self.capacity
    #     0   1
    #   [[], []]

    def get_num_slots(self):
        return self.capacity


    def get_load_factor(self):
        pass

    def fnv1(self, key):
        hash = 14695981039346656037
        bytes_representation = key.encode()

        for byte_of_data in bytes_representation:
            hash *= 1099511628211
            hash = hash ^ byte_of_data
        return hash

    def djb2(self, key):
        pass


    def hash_index(self, key):
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        
        new_node = HashTableEntry(key, value)

        if self.head is None:
            self.head = new_node
        else:
            self.head.next(new_node)
            self.head = new_node
            self.size += 1


    def delete(self, key):
        self.put(key, None)
        self.size -= 1


    def get(self, key):
        index = self.hash_index(key)

        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur.key
            cur = cur.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
