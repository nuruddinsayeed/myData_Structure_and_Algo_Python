class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None] * 26
        self.isWord = False


class Tries:
    def __init__(self):
        self.root = Node('a')

    def insert(self, word: str):
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = Node(c)
            curr = curr.children[index]
        curr.isWord = True

    def search(self, word: str):
        node = self.get_node(word)
        return node is not None and node.isWord

    def start_with(self, word: str):
        return self.get_node(word) is not None

    def get_node(self, word: str):
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is not None:
                curr = curr.children[index]
            else:
                return None
        return curr


tries = Tries()
tries.insert("word")
print(tries.search("wor"))
print(tries.search("word"))
print(tries.start_with("woj"))
