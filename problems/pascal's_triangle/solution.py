class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 1:
            result.append([1])
            return result
        elif numRows == 2:
            result.append([1])
            result.append([1,1])
            return result
        result.append([1])
        result.append([1,1])
        for i in range(2,numRows):
            p = [1]*(i+1)
            for j in range(1,len(p)-1):
                p[j] = result[i-1][j-1]+result[i-1][j]
            result.append(p)
        return result