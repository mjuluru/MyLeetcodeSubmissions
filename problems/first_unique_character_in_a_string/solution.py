class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos = []
        for k, v in Counter(s).items():
            if v == 1:
                pos.append(s.index(k))
        if pos:
            return min(pos)
        else:
            return -1