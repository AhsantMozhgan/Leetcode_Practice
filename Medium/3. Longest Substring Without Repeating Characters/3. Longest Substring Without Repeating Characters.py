# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen_characters = set()  # This set will store the characters in the current substring
        left = 0  # This is the left pointer for the sliding window
        longest_length = 0  # Variable to keep track of the longest substring length

        for right in range(len(s)):  # Right pointer iterating through the string
            # If the character at 'right' is already in the set, shrink from the left
            while s[right] in seen_characters:
                # Remove the character at the left pointer from the set
                seen_characters.remove(s[left])  
                left += 1  # Move the left pointer to the right
                
            seen_characters.add(s[right])  # Add the current character at 'right' to the set
            
            # Update the longest length found so far
            longest_length = max(longest_length, right - left + 1)

        return longest_length  # Return the length of the longest substring found
        