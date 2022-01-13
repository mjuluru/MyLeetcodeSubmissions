class Solution:
    def maxArea(self, height: List[int]) -> int:
        # result = 0
        # for i in range(0, len(height)):
        #     for j in range(i+1, len(height)):
        #         area = min(height[i], height[j])*(j-i)
        #         if result < area:
        #             result = area
        # return result
        
        result = 0 
        l = 0
        r = len(height)-1
        while(l<r):
            area = min(height[l], height[r]) * ( r-l )
            if result < area:
                result = area
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return result