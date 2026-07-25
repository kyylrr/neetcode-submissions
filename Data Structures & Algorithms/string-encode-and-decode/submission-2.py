class Solution:

    def encode(self, strs: List[str]) -> str:
        word =''
        for i in strs:
            word += str(len(i)) + '#'+ i
        return word

    def decode(self, s: str) -> List[str]:
        answer = []
        i=0
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            num = int(s[i:j])
            answer.append(s[j+1:j+num+1])
            i= j+num+1
        return answer