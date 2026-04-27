class TrieNode:
    def __init__(self):
        self.children = {} # char => TrieNode (next characters)
        self.is_word = False # marks end of word

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                new_node = TrieNode()
                cur.children[ch] = new_node
                cur = new_node
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        return True
        