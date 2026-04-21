# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        count=0
        while curr is not None:
            curr=curr.next
            count+=1
        hehe=head
        mid=count//2
        while mid > 0:
            hehe=hehe.next
            mid-=1
        return hehe

                

