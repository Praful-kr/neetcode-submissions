class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}  # mappign the char count to list of anagrams
        for s in strs:
            count = [0] * 26  # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)      # in python lists cannot be keys, so changed to tuples
            if key not in res:
                res[key] = []
            res[key].append(s)  

        return list(res.values())