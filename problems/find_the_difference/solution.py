class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i in s:
                if s.count(i) == t.count(i):
                    continue
                else:
                    return i
            else:
                return i
