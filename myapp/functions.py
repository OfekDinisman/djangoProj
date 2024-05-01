class Solution:
    #Given an integer x, return true if x is a palindrome, and false otherwise.
    @staticmethod
    def is_palindrome(x: int) -> bool:
        x_str=str(x)
        if len(x_str)==1:
            return True
     
        if x_str[0]=='-':
            return False
        left=0
        right=len(x_str)-1
        while left<right:
            if x_str[left]!=x_str[right]:
                return False

            left+=1
            right-=1
        return True