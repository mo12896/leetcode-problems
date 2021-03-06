# 206. Reverse Linked List (Easy)
# https://leetcode.com/problems/reverse-linked-list/submissions/
# https://www.youtube.com/watch?v=NCilGMhdYPY&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head): # O(N) time, O(1) space
        prev = None
        while head: # O(N) time, O(1) space
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev