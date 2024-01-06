# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyL = []
    
        for L in lists:
            while L:
                dummyL.append(L.val)
                L = L.next

        dummyL.sort()
        dummy = ListNode()
        cur = dummy
        for i in dummyL:
            cur.next = ListNode(i)
            cur = cur.next

        return dummy.next


