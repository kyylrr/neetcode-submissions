class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        
        
        needmap = defaultdict(int)
        havemap = defaultdict(int)
        for i in range(len(t)):
            needmap[t[i]] +=1
        have = 0
        need = len(needmap)
        l=0
        res = ""
        resLen = float('infinity')
        for r in range(len(s)):
            if s[r] in needmap:
                havemap[s[r]] +=1
                if havemap[s[r]] == needmap[s[r]]:
                    have +=1
            while have == need: 
                if r-l+1 <= resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                havemap[s[l]] -= 1
                if s[l] in needmap and havemap[s[l]] < needmap[s[l]]:
                    have -= 1
                l += 1    
        return res