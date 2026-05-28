class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        time_value = self.store[key]
        if not time_value: return ""

        l, r = 0, len(time_value) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            if time_value[m][0] <= timestamp:
                res = time_value[m][1]
                l = m + 1
            else:
                r = m - 1

        return res


