class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            index = ord(ch)-ord("a")
            if not node.links[index]:
                node.links[index] = TrieNode()
            node = node.links[index]
        node.is_end = True


    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if not node.links[index]:
                return False
            node= node.links[index]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            index = ord(ch) - ord("a")
            if not node.links[index]:
                return False
            node= node.links[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)