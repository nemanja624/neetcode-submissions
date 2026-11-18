class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        goto = [{}]
        fail = [0]
        out = [-1]
        word_at = [-1]

        for idx, w in enumerate(words):
            node = 0
            for ch in w:
                if ch not in goto[node]:
                    goto.append({})
                    fail.append(0)
                    out.append(-1)
                    word_at.append(-1)
                    goto[node][ch] = len(goto) - 1
                node = goto[node][ch]
            word_at[node] = idx

        queue = deque(goto[0].values())
        while queue:
            node = queue.popleft()
            for ch, nxt in goto[node].items():
                f = fail[node]
                while f and ch not in goto[f]:
                    f = fail[f]
                fail[nxt] = goto[f].get(ch, 0)
                out[nxt] = fail[nxt] if word_at[fail[nxt]] != -1 else out[fail[nxt]]
                queue.append(nxt)

        found = [False] * len(words)

        for idx, w in enumerate(words):
            node = 0
            for ch in w:
                while node and ch not in goto[node]:
                    node = fail[node]
                if ch in goto[node]:
                    node = goto[node][ch]

                m = node if word_at[node] != -1 else out[node]
                while m != -1:
                    wid = word_at[m]
                    if wid != idx:
                        if found[wid]:
                            break
                        found[wid] = True
                    m = out[m]

        return [words[i] for i in range(len(words)) if found[i]]