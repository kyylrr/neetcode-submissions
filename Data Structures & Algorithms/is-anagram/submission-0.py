class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        answer = False
        
        s = sorted(s)
        t = sorted(t)
        if(s == t):
            answer = True
        return answer