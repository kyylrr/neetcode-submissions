class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        answer=0
        while left<right:
            width = right - left
            area = min(heights[left], heights[right])*width
            answer =max(answer, area)
            if heights[left] < heights[right]:
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else: 
                right-=1
        return answer