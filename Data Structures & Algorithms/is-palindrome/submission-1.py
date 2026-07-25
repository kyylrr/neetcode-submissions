class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = "".join(char.lower() for char in s if char.isalnum())

        left =0
        right = len(cs)-1
        while left<right:
            if cs[left]!= cs[right]:
                return False
            
            left +=1
            right -=1
        return True