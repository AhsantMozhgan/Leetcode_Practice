# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Base cases for n = 1 and n = 2
        if n <= 2:
            return n

        # Create an array to store the number of ways to reach each step
        ways = [0] * (n + 1)

        # Base case initializations
        ways[1] = 1  # There is 1 way to get to the first step
        ways[2] = 2  # There are 2 ways to get to the second step

        # Fill the ways array for steps from 3 to n
        for current_step in range(3, n + 1):
            ways[current_step] = ways[current_step - 1] + ways[current_step - 2]
            

        # Return the number of ways to reach the nth step
        return ways[n]


# This is a dynamic programming problem.  

# The key insight is that to reach step n you can only come from step n-1 (by taking one step) or from step n-2 (by taking two steps). 
#So the number of ways to reach n is just the sum of the ways to reach n-1 and n-2.  

# I keep an array where `ways[current_step]` stores the number of ways to reach step current_step.
# I set the base cases for steps 1 and 2, then fill the rest of the array from 3 up to n using that recurrence.  

# At the end I return `ways[n]`.  

# It runs in O(n) time and uses O(n) space.
