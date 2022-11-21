'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
#TC=O(n)
#SC=O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
#TC=O(nlogn)
#SC=O(1)
