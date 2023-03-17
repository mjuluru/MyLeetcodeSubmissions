class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        og_r = len(mat)
        og_c = len(mat[0])
        if og_r*og_c != r*c:
            return mat
        elif og_r == r and og_c == c:
            return mat
        
        result = [[0 for j in range(c)] for i in range(r)]
        
        k = 0
        l = 0
        count = 0
        for i in range(og_r):
            for j in range(og_c):
                count += 1
                result[k][l] = mat[i][j]
                l+=1
                if count == c:     
                    k = k + 1
                    l = 0
                    count = 0
        return result