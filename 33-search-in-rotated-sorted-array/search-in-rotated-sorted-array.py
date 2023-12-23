class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # without binary search it is easy just apply for loop
        n = len(nums)

        start = 0
        end = n-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            # Left sorted portion
            if nums[start] <= nums[mid]:
                if target < nums[start] or target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            # Right sorted portion
            else:
                if target > nums[end] or target < nums[mid]:
                    end = mid -1
                else:
                    start = mid+1
                
            
        return -1