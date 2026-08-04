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



# “I’d use a hash map to store each number and its index as I iterate through the array.  

# For every number, I calculate its complement — target minus the current number.  
# If that complement is already in the map, I’ve found the pair, so I immediately return the stored index of the complement and the current index.  

# If it’s not there, I just add the current number and its index to the map and keep going.  

# This way I only make a single pass, so it’s O(n) time and O(n) extra space.”