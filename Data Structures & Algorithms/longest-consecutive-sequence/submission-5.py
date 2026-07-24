class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count =1
        sorte = sorted(nums)
        array = [1]
        if len(nums) == 0:
            return 0
        if len(nums )==1:
            return 1
        for i in range(len(sorte) -1, -1, -1):
            if(sorte[i-1] == sorte[i] ):
                continue
            elif(sorte[i-1] == sorte[i] -1 ):
                count +=1
            else:
                array.append(count)
                count = 1;
        return max(array)            