class PrefixNode:
    def __init__(self):
        self.characters = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                cur.characters[c] = PrefixNode()
            cur = cur.characters[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                return False
            cur = cur.characters[c]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.characters:
                return False
            cur = cur.characters[c]
        return True