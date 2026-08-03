# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_to_index = dict()  # Dictionary to hold number and its index
        # num_to_index = {}
        
        for index, num in enumerate(nums):
            required_number = target - num  # Calculate the required_number
            if required_number in num_to_index:
                # Return indices of the two numbers
                return [num_to_index[required_number], index]  
            num_to_index[num] = index  # Add number to the dictionary
            
        return []  # Return an empty list if no solution is found (though problem guarantees one solution)
