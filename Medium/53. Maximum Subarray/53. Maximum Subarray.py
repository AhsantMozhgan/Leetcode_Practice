# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_current = max_global = nums[0]  # Initialize with the first element

        for i in range(1, len(nums)):
            # Choose the max between current element and the sum up to the current element.
            max_current = max(nums[i], max_current + nums[i])  
            
            if max_current > max_global:
                max_global = max_current  # Update the maximum found so far

        return max_global


# I’d use Kadane’s algorithm.  

# I keep two variables: `max_current`, the best subarray sum ending at the current index, and `max_global`, the best sum I’ve seen overall.  

# For each number I decide whether to start a brand-new subarray at this point or extend the previous one — I just take the maximum of the number itself and `max_current + number`.  

# Then I update `max_global` whenever `max_current` is bigger.  

# At the end, `max_global` holds the maximum subarray sum.  

# It runs in O(n) time and uses only O(1) extra space.