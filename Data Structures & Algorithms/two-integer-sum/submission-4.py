class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #This solution is O(n) time and space complexity and uses hashmap technique       
        prevMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return[prevMap[diff], i]
            else:
                prevMap[nums[i]] = i
        return