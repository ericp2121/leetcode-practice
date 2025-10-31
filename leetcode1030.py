# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):no 
        dummy = ListNode(0)      # create a dummy node before head, in case that head is to be removed there would be issue in where head reference is to
        dummy.next = head # set the next (ie head) to point to head, ie inserts dummy head 0 at start and then makes it point to prev head 
        current = dummy # set current to start checking at dummy 

        # dummy value does not matter, always start at dummy.next

        while current.next is not None:
            # iterates through the list until it reaches end (ie next is end)
            # ensuring that the next node is not empty 
            if current.next.val == val:
                current.next = current.next.next
                # if current node is equal to target num, delete it by changing its reference to the node after
            else:
                current = current.next
                # if not target node. interate node up one 
                # keep moving dodwn list

        return dummy.next  # return new head, return the actual head (ie dummy.next),full list after deletion done. 
