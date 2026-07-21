class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        for num in range(len(nums)-1):
            for sec in range(num+1, len(nums)):
                if (nums[num]+nums[sec]==target):
                    list.append(num)
                    list.append(sec)
                    return list
      