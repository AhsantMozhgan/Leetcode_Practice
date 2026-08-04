# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode()  # Create a dummy head for the new merged list
        current = dummy_head  # Pointer to build the new list

        # Traverse both lists while they are not empty
        while list1 and list2:
            # Compare the current nodes of both lists
            if list1.val <= list2.val:
                current.next = list1  # Attach the smaller node
                list1 = list1.next  # Move to the next node in list1
            else:
                current.next = list2  # Attach the smaller node
                list2 = list2.next  # Move to the next node in list2

            current = current.next  # Move the current pointer forward

        # At the end of the loop, one of the lists may still have nodes
        # Attach whichever list still has remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return the next node of dummy head which points to the merged list
        return dummy_head.next


# I’d merge the two sorted lists using a dummy head and a pointer that always points to the end of the merged list.

# While both lists still have nodes, I compare their current heads, attach the smaller one to the merged list, and advance that list’s pointer. I also move my merged-list pointer forward each time.

# Once one of the lists runs out, I simply attach whatever is left of the other list, since it’s already sorted.

# Finally I return `dummy.next` as the head of the merged list.  

# This runs in O(m + n) time and uses only O(1) extra space.
