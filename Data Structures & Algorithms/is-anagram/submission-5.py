class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = [0] * 26

        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1      #increment for every occurance of character
            counter[ord(t[i]) - ord('a')] -= 1      #decrement
        
        return all(c==0 for c in counter)           #returns true is all values of counter are 0 otherwise false