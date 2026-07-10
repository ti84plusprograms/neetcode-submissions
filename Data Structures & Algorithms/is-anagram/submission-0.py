class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        if s == t:
            return True
        
        new_s = sorted(s)
        new_t = sorted(t)

        return new_s == new_t

        
        # for char in s:
        #     if char not in t:
        #         return False
        # return True
            
        