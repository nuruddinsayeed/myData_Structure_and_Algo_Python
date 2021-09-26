class Node:
    def __init__(self, val) -> None:
        self.prev = None
        self.next = None
        self.val = val


class LinkedListDouble:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    # def add(self, val):
    #     # add at the end of the node
    #     node = Node(val)

    #     if self.head is not None:
    #         self.tail.next = node
    #         node.prev = self.tail
    #     else:
    #         self.head = node
    #     self.tail = node
    #     self.size += 1
    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.size += 1

    def __rm_node(self, node):
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

    def remove(self, val):
        # remove certain value
        node = self.head
        while node is not None:
            if node.val == val:
                self.__rm_node(node)
                self.size -= 1
            node = node.next

    def __str__(self) -> str:
        values = []
        node = self.head

        while node is not None:
            values.append(node.val)
            node = node.next
        return f"[{', '.join(str(value) for value in values)}]"

    # def lamdaExpPrac(self):
    #     #full_name = lambda first_name, last_nam: first_name.strip().title()+ " " + last_nam.strip().title()
    #     pass


my_list = LinkedListDouble()
my_list.add(1)
my_list.add(54)
my_list.add(3)
my_list.add(5)
my_list.add(74)
my_list.add(0)
my_list.add(5)
my_list.add(5)
print(my_list)
print(my_list.size)

my_list.remove(5)
print(my_list)
print(my_list.size)
