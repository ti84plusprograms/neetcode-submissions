class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for str_ in strs:
            key = "".join(sorted(str_))
            if key not in anagrams:
                anagrams[key] = [str_]
            else:
                anagrams[key].append(str_)
        
        res = [lst for lst in anagrams.values()] 

        return res