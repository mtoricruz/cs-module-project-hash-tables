class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def set_next(self, new_next):
        self.next = new_next


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_to_head(self, value):
        value.next = self.head
        self.head = value


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.size = 0
        # self.hash = [None] * self.capacity
        self.hash = [LinkedList()] * self.capacity
    #     1  2
    #   [[], []]

    def get_num_slots(self):
        return self.capacity


    def get_load_factor(self):
        return self.size / self.capacity
        
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash = 14695981039346656037
        bytes_representation = key.encode()

        for byte_of_data in bytes_representation:
            hash *= 1099511628211
            hash = hash ^ byte_of_data
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Beej mentioned keep increment counter for size. do i put
        # size += 1 under each pos.key if statement
        index = self.hash_index(key)
        cur = self.hash[index].head
        
        while cur:
            if cur.key == key:
                cur.value = value
            cur = cur.next
        
        new_entry = HashTableEntry(key, value)
        self.hash[index].add_to_head(new_entry)
        self.size += 1


    def delete(self, key):
        self.put(key, None)
        self.size -= 1


    def get(self, key):
        index = self.hash_index(key)
        cur = self.hash[index].head

        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None


    def resize(self, new_capacity):
        if self.get_load_factor() >= 0.7:
            old_hash = self.hash
            self.hash = [LinkedList()] * new_capacity
            for i in old_hash:
                cur = i.head
                while cur:
                    self.put(cur.key, cur.value)
                    cur = cur.next
                self.capacity = new_capacity



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
