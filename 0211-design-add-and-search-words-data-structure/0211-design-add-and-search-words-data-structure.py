class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord("a")
            if not node.child[index]:
                node.child[index] = TrieNode()
            node = node.child[index]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for child in node.child:
                        if child and dfs(i + 1, child): #go down the different paths
                            return True
                    return False #if we get to this point then no available path
                else:
                    index = ord(char) - ord("a")
                    if not node.child[index]:
                        return False
                    node = node.child[index]
            return node.is_end

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)