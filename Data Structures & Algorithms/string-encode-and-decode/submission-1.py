class Solution:
    def encode(self, strs: List[str]) -> str:
        answer = ''
        for words in strs:
            answer = answer+f"{len(words)}" + "#" +words
        return answer

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s) :
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+ length])
            i= j+1+ length
        return res