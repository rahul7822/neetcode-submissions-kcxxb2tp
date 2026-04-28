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
                return True

            for i in range(index, len(word)):
                if word[i] != "." and word[i] in cur.children:
                    res = backtrack(cur.children[word[i]], i + 1)
                    if res:
                        return True
                elif word[i] == "." and len(cur.children) != 0:
                    for key in cur.children.keys():
                        res = backtrack(cur.children[key], i + 1)
                        if res:
                            return True
                else:
                    return False

        return backtrack(root, 0)
