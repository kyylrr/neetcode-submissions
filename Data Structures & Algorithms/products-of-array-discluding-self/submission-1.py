class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer =[]
        for i in range(len(nums)):
            j=0
            holder=1;
            while(j<len(nums)):
                if j == i:
                    j+=1
                else:
                    holder *=nums[j]
                    j+=1
            answer.append(holder)
        return answer
