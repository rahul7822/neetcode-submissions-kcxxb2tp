class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_word = True
    
    def search(self, word: str) -> bool:
        root = self.root
        
        def backtrack(cur, index):
            if index == len(word):
                return cur.is_word

            ch = word[index]
            if ch != ".":
                if ch not in cur.children:
                    return False
                return backtrack(cur.children[ch], index + 1)
            else:
                if len(cur.children) != 0:
                    for key in cur.children.keys():
                        res = backtrack(cur.children[key], index + 1)
                        if res:
                            return True
                    return False
                else:
                    return False

        return backtrack(root, 0)
