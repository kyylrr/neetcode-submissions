class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis = []
        for num in range(len(nums)-1):
            for sec in range(num+1, len(nums)):
                if (nums[num]+nums[sec]==target):
                    lis.append(num)
                    lis.append(sec)
                    return lis
      