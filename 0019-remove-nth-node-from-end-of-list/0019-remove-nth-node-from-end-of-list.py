# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = slow = dummy

        # fast를 n+1칸 이동 → slow가 삭제할 노드의 이전 노드에 위치하게 됨
        for _ in range(n + 1):
            fast = fast.next

        # fast와 slow 동시에 이동
        while fast:
            fast = fast.next
            slow = slow.next

        # slow.next가 삭제 대상
        slow.next = slow.next.next

        return dummy.next
        