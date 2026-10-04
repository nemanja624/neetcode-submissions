class PrefixNode:
    def __init__(self):
        self.characters = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                cur.characters[c] = PrefixNode()
            cur = cur.characters[c]
        cur.is_word = True           

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.characters.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.characters:
                        return False
                    cur = cur.characters[c]
            return cur.is_word

        return dfs(0, self.root)