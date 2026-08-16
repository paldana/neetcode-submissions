class Node:
    def __init__ (self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}     # key: int num; value: node

        # # initialize MRU and LRU nodes
        # self.lru, self.mru = Node(0, 0), Node(0, 0)
        # self.lru.next = self.mru
        # self.mru.prev = self.lru
        
        # set dummy nodes for LRU and MRU pointers
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def get(self, key: int) -> int:
        # return -1 if key DNE
        if key not in self.cache:
            return -1
        
        ## update the MRU LL to put the recently retrieved node to be at the MRU
        # - one way to do this is by removing the existing key from the LL 
        #   and then inserting it back to the LL and be the MRU node
        targetNode = self.cache[key]
        self.remove(targetNode)
        self.insert(targetNode)
        
        # return the value of the node
        return targetNode.val


    def put(self, key: int, value: int) -> None:
        # add the key-value or update the value if key exists in the cache 
        # and create a node to be INSERTED to the linked list
     
        ## update the node in the LL if key already exists
        if key in self.cache:
            self.remove(self.cache[key])     # remove existing node
        
        ## insert new node
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        # self.cache[key] = Node(key, value)
        # self.insert(self.cache[key])
        
        ## if after adding the new key-value pair make the LL exceed capacity,
        # remove the LRU node to remain within cap
        if len(self.cache) > self.cap:
            lruNode = self.lru.next
            self.remove(lruNode)
            del self.cache[lruNode.key]


    ## additional functions - insert and remove
    def insert(self, node: Node):
        left, right = self.mru.prev, self.mru
        left.next = right.prev = node
        node.prev, node.next = left, right 
        return

    def remove(self, node: Node):
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        return

