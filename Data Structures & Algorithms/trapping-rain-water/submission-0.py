class Solution:
    def trap(self, height: List[int]) -> int:
       
       l = 0
       r = len(height) -1
       res =0
       maxl = height[l]
       maxr = height[r]
       while l < r:
        if maxl > maxr:
            r -=1
            curarea = maxr- height[r] 
            if curarea <0:
                curarea = 0
                maxr =height[r]
            res +=curarea

        elif maxl < maxr or maxl == maxr:
            l +=1
            curarea =   maxl- height[l]
            if curarea <0:
                curarea = 0
                maxl =height[l]

            res +=curarea
       return res

       