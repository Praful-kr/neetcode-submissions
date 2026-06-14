class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    #The above function is inbuilt function in python which counts the character in a string 
    #and then returns if count of every character is same or not
    # -> This might not be directly used in interview