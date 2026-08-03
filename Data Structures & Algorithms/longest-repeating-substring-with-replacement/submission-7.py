class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        mapval = collections.defaultdict(int)
        for r in range(len(s)):
            mapval[s[r]] +=1
            if ((r-l) - max(mapval.values()) >= k):
                mapval[s[l]] -=1
                l += 1
            res = max(res, r-l+1)
            
        return res