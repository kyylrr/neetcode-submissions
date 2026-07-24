class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        answer = False;
        for num in range(len(nums) - 1):
           if nums[num] == nums[num+1]:
            answer = True
            break
        return answer
                
