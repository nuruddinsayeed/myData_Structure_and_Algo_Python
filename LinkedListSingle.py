class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        self.size -= 1

        return value

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.head.value

    def __len__(self):
        return self.size


# my_stack = Stack()
# my_stack.push(3)
# my_stack.push(5)
# print(my_stack.peek())
# my_stack.push(45)
# my_stack.push(1)
# my_stack.push(9)
# print(len(my_stack))
# print(my_stack.pop())
# print(len(my_stack))
# print(my_stack.pop())
# print(len(my_stack))

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)

        if self.head is not None:
            self.head.next = node
        else:
            self.tail = node
        self.head = node
        self.size += 1

    def dequeue(self):
        if self.tail.next is None:
            self.head = None
        value = self.tail.value
        self.tail = self.tail.next
        self.size -= 1
        return value

    def front(self):
        return self.tail.value

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        return f"Size: {self.size}, Head: {self.head}, Tail: {self.tail}"


# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# print(f"front: {my_queue.front()}")
# print(f"Dequeue: {my_queue.dequeue()}")
# print(f"Size: {len(my_queue)}")
# print(f"front: {my_queue.front()}")