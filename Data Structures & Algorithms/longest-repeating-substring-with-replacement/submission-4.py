class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        table = defaultdict(int)
        res =0
        for r in  range(len(s)):
            table[s[r]] += 1
            
            if ((r-l)-max(table.values()) >= k):
                table[s[l]] -=1
                l +=1
            res = max(res, r-l +1)
        return res
