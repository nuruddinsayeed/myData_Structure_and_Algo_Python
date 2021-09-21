
from BinaryTreePrinter import BinaryTreePrinter


class Tree:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        """Insert value to cosest tree node"""
        tree_node = Tree(val)

        if self.root is None:
            self.root = tree_node
            return

        currNode = self.root
        nodes = []
        while True:
            if currNode.left is None:
                currNode.left = tree_node
                return
            elif currNode.right is None:
                currNode.right = tree_node
                return
            nodes.append(currNode.left)
            nodes.append(currNode.right)
            currNode = nodes.pop(0)

    def __str__(self) -> str:
        treePrinter = BinaryTreePrinter()
        return treePrinter.get_tree_string(self.root)


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Tree(val)
            return
        self.__insert_value(self.root, val)

    def __insert_value(self, node, val):
        if val == node.value:
            return
        elif val < node.value:
            if node.left is None:
                node.left = Tree(val)
                return
            self.__insert_value(node.left, val)
        else:
            if node.right is None:
                node.right = Tree(val)
            self.__insert_value(node.right, val)

    def inorder_print(self):
        self.__inorder_print(self.root)

    def __inorder_print(self, node):
        if node is None:
            return
        else:
            self.__inorder_print(node.left)
            print(node.value, end=" ")
            self.__inorder_print(node.right)

    def contains(self, val):
        if self.root is None:
            return False
        node = self.root
        while node is not None:
            if node.value == val:
                return True
            elif node.value > val:
                node = node.left
            else:
                node = node.right
        return False

    def __str__(self):
        treePrinter = BinaryTreePrinter()
        return treePrinter.get_tree_string(self.root)


#         # Test Binary Tree
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

my_BST = BST()
for i in [25, 12, 18, 42, 9, 4, 71, 85, 19, 14, 11, 12, 17, 29, 44, 45, 1, 33, 37, 18, 14, 28]:
    my_BST.insert(i)
print(my_BST)
my_BST.inorder_print()
print("\n Contains 25?", my_BST.contains(25))
print("\n Contains 45?", my_BST.contains_using_stack(45))
print("\n Contains 45?", my_BST.contains(45))
print("\n Contains 43?", my_BST.contains_using_stack(43))
