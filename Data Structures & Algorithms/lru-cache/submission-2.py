class Node: 
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None            # Doubly Linked List (DLL)


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}         # cache = key: int, value: Node

        # set dummy nodes for LRU and MRU pointers
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def insert(self, node: Node) -> None: 
        left, right = self.mru.prev, self.mru

        # update pointers of existing nodes first 
        left.next = node
        right.prev = node

        # update pointers of newly inserted node
        node.prev = left
        node.next = right

    def remove(self, node: Node) -> None:
        # get nodes next to the node to be removed first
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

    ## Will not work if the node to be deleted is somewhere in the middle of the DLL
    ## -> This will only work if we're removing the LRU only all the time
    # def remove(self, node: Node) -> None:
    #     left, right = self.lru, self.lru.next
    #     # update pointers to remove the LRU (right of self.lru)
    #     newLru = right.next
    #     left.next = newLru
    #     newLru.prev = left


    def get(self, key: int) -> int:
        # remove and re-add node so it'll be the MRU in the cache
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        # check if key is in the cache, if it is, remove node and add new node
        if key in self.cache:
            self.remove(self.cache[key])
        
        # add key value pair to cache and insert to the DLL
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        # check if cache is at capacity
        if len(self.cache) > self.cap:
            # remove LRU from cache and update pointers 
            lruNode = self.lru.next         # get LRU node 
            self.remove(lruNode)            # remove from DLL
            del self.cache[lruNode.key]     # remove from cache
            
