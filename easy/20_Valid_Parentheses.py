# Definition for singly-linked list.
from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return sorted(list1 + list2)

test = Solution()
print(test.mergeTwoLists([1,2,4], [1,3,4]))