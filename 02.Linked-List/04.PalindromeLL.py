class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast , slow = head, head
        
        #find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse 2nd half
        prev = None
        while slow:
            tmp  = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        #check
        l,r=head,prev
        while r:
            if l.val != r.val:
                return False
            l=l.next
            r=r.next
        return True
            
