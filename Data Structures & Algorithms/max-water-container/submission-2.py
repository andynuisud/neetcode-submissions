class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = float('-inf')
        left = 0 
        right = len(heights)-1

        while left <= right: 
            
            currentArea = min(heights[right], heights[left]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1

        return maxArea
