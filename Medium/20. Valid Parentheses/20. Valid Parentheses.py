# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets waiting to be matched.
        opening_brackets = []

        # Mapping of each opening bracket to its corresponding closing bracket.
        matching_brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        # Process each character in the input string.
        for current_character in s:
            # If we find an opening bracket, save it.
            if current_character in matching_brackets:
                opening_brackets.append(current_character)

            # Check if the current character is a closing bracket 
            # that matches the top of the stack.
            elif (
                opening_brackets
                and current_character == matching_brackets[opening_brackets[-1]]
            ):
                opening_brackets.pop()  # Remove the matched opening bracket.

            # If we encounter a closing bracket that doesn't match or the stack is empty, return False.
            else:
                return False

        # At the end, check if the stack is empty. all brackets must be matched.
        return len(opening_brackets) == 0


# I’d use a stack to keep track of unmatched opening brackets.  
# I also keep a map from each opening bracket to its corresponding closing bracket.  

# As I iterate through the string:  
# - If I see an opening bracket, I push it onto the stack.  
# - If I see a closing bracket, I check that the stack is not empty and that it matches the bracket at the top of the stack. If both are true, I pop the top. Otherwise I return false immediately.  

# At the end, the string is valid only if the stack is empty — meaning every opening bracket found its match.


# OR
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []  # Initialize an empty stack
#         bracket_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets

#         for char in s:
#             if char in bracket_map:  # If it's a closing bracket
#                 # Pop from stack if not empty, else use a dummy value
#                 top_element = stack.pop() if stack else '#'

#                 # Check if the popped bracket matches the corresponding opening bracket
#                 if bracket_map[char] != top_element:
#                     return False
#             else:
#                 # It's an opening bracket, push it onto the stack
#                 stack.append(char)

#         # If stack is empty, all brackets matched correctly
#         return not stack


# I’d use a stack to track unmatched opening brackets, and a map from each closing bracket to its matching opening bracket.

# As I go through the string:

# - If I see a closing bracket, I pop the top of the stack (or use a dummy value if the stack is empty) and check whether it matches the expected opening bracket from the map. If it doesn’t match, I return false right away.
# - If I see an opening bracket, I just push it onto the stack.

# At the end the string is valid only if the stack is empty, that means every opening bracket found its match.”
