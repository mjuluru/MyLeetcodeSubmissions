class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        r = Counter(ransomNote)
        for k,v in r.items():
            if k in m.keys() and v <= m[k]:
                continue
            return False
        return True