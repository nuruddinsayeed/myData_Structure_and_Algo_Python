from BinaryTreePrinter import BinaryTreePrinter
from LinkedListSingle import Queue, Stack


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            current_node = self.root
            queue = Queue()
            while True:
                if current_node.left is None:
                    current_node.left = TreeNode(value)
                    return
                elif current_node.right is None:
                    current_node.right = TreeNode(value)
                    return
                else:
                    queue.enqueue(current_node.left)
                    queue.enqueue(current_node.right)
                    current_node = queue.dequeue()

    def contains(self, value):
        nodes = Stack()
        nodes.push(self.root)

        while nodes.size != 0:
            node = nodes.pop()
            if node.value == value:
                return True
            elif node.right is not None:
                nodes.push(node.right)
                if node.left is not  None:
                    nodes.push(node.left)
        return False

    def __str__(self):
        treePrinter = BinaryTreePrinter()
        return treePrinter.get_tree_string(self.root)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.__inset_value(self.root, value)

    def __inset_value(self, node, value):

        if node.value == value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                return
            self.__inset_value(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                return
            self.__inset_value(node.right, value)

    def inorder_print(self):
        self.__inorder_print(self.root)

    def __inorder_print(self, node):
        if node is None:
            return
        else:
            self.__inorder_print(node.left)
            print(node.value, end=" ")
            self.__inorder_print(node.right)

    def contains(self, value):
        node = self.root
        while node is not None:
            if node.value == value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def contains_using_stack(self, value):
        nodes = Stack()
        nodes.push(self.root)

        while nodes.size != 0:
            node = nodes.pop()
            if node.value == value:
                return True
            elif value < node.value:
                if node.left is not None:
                    nodes.push(node.left)
            else:
                if node.right is not None:
                    nodes.push(node.right)
        return False

    def __str__(self):
        treePrinter = BinaryTreePrinter()
        return treePrinter.get_tree_string(self.root)


# my_BST = BST()
# for i in [25, 12, 18, 42, 9, 4, 71, 85, 19, 14, 11, 12, 17, 29, 44, 45, 1, 33, 37, 18, 14, 28]:
#     my_BST.insert(i)
# print(my_BST)
# my_BST.inorder_print()
# print("\n Contains 25?", my_BST.contains(25))
# print("\n Contains 45?", my_BST.contains_using_stack(45))
# print("\n Contains 45?", my_BST.contains(45))
# print("\n Contains 43?", my_BST.contains_using_stack(43))

# my_tree = BinaryTree()
# for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#              'E']:
#     my_tree.insert(char)
# print(my_tree)

# my_tree2 = BinaryTree()
# for char in [25, 12, 18, 42, 9, 4, 71, 85, 19, 14, 11, 12, 17, 29, 44, 45, 1, 33, 37, 18, 14, 28]:
#     my_tree2.insert(char)
# print(my_tree2)
# print("Contains 25? ", my_tree2.contains(25))
# print("Contains 45? ", my_tree2.contains(45))
# print("Contains 43? ", my_tree2.contains(43))