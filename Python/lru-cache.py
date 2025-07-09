from typing import Dict


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkList:
    def __init__(self):
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def remove_end(self) -> Node:
        if self.tail.prev == self.head:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node

    def move_to_front(self, node: Node):
        self.remove_node(node)
        self.add_to_front(node)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.size: int = 0
        self.location: Dict[int, Node] = {}
        self.double_link_list: DoubleLinkList = DoubleLinkList()

    def get(self, key: int) -> int:
        if key not in self.location:
            return -1
        node: Node = self.location[key]
        self.double_link_list.move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.location:
            self.location[key].value = value
            self.double_link_list.move_to_front(self.location[key])
            return
        node = None
        if self.size == self.capacity:
            self.size -= 1
            node_to_remove: Node = self.double_link_list.remove_end()
            self.location.pop(node_to_remove.key)
            node = node_to_remove
        if not node:
            node = Node(0, 0)
        node.key = key
        node.value = value
        self.location[key] = node
        self.double_link_list.add_to_front(node)
        self.size += 1


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1
    cache.put(3, 3)  # evicts key 2
    print(cache.get(2))  # returns -1 (not found)
    cache.put(4, 4)  # evicts key 1
    print(cache.get(1))  # returns -1 (not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4
