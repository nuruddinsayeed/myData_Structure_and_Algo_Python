class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

class LinkedListDouble:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.size += 1

    def remove(self, value):
        node = self.head

        while node is not None:
            if node.value == value:
                self.__remove_node(node)
                self.size -= 1
                break
            node = node.next

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
            if node.next is not None:
                self.head.prev = None
        elif node.next is None:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def __str__(self):
        values = []
        node = self.head

        while node is not None:
            values.append(node.value)
            node = node.next
        return f"[{', '.join(str(value) for value in values)}]"

my_linked_list = LinkedListDouble()
my_linked_list.add(5)
my_linked_list.add(46)
my_linked_list.add(13)
my_linked_list.add(8)

print(my_linked_list)

my_linked_list.remove(46)
print(my_linked_list)
my_linked_list.remove(5)
print(my_linked_list)
my_linked_list.remove(8)
print(my_linked_list)
my_linked_list.remove(13)

print(my_linked_list)
print(my_linked_list.size)
