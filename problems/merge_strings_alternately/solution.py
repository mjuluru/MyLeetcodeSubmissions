class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = ""
        for i,j in zip(range(len(word1)), range(len(word2))):
            sol += word1[i]
            sol += word2[j]
        if i < len(word1):
            sol += word1[i+1:]
        if j < len(word2):
            sol += word2[j+1:]
        return sol
