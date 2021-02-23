class Node:
    
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.addAtHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            self.addAtHead(node)
        else:
            node = Node(key, value)
            if len(self.map) >= self.capacity:
                self.removeFromTail()
            self.addAtHead(node)
            self.map[key] = node
                
        
    def addAtHead(self, node):
        _next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = _next
        _next.prev = node

    def removeFromTail(self):
        if self.tail.prev!= self.head:
            end = self.tail.prev
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
        del self.map[end.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)