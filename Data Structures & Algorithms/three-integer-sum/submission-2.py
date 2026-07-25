class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        base =0
        answer =[]
        nums.sort()
        for base in range( len(nums)-2):
            if base > 0 and nums[base] == nums[base - 1]:
                continue

            goal = nums[base]*(-1)
            left = base +1
            right = len(nums)-1

            while left < right:
                if goal == nums[left] +nums[right]:
                    answer.append([nums[base], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif goal < nums[left] + nums[right]:
                    right -=1
                elif goal > nums[left]+nums[right]:
                    left+=1                
        return answer

        