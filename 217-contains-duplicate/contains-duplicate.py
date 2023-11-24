class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using brute force..T:O(n^2)
        # n = len(nums)
        # for i in range(0,n): 
        #     for j in range(i+1,n):
        #         if(nums[i] == nums[j]):
        #             return True
        # else: 
        #     return False     

        #Using Hash Set: T:O(n)
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        return False
        