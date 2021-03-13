# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
          :type l1: ListNode
          :type l2: ListNode
          :rtype: ListNode
        """

        l3begin = None
        cur = None
        carry = 0

        while l1 or l2 or carry:

            print('Here 1')
            l3 = ListNode(val=0, next=None)
            if l3begin is None:
                l3begin = l3
                cur = l3begin
            else:
                cur.next = l3
                cur = cur.next

            l3.val = (l1.val if l1 else 0 )+ (l2.val if l2 else 0) + carry
            print(f'l3.val is {l3.val} l2 is {(l2.val if l2 else 0)} l1 is {(l1.val if l1 else 0 )}' )

            if l3.val >= 10:
                carry = l3.val // 10
                l3.val = l3.val % 10
            else:
                carry = 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return l3begin


def printll(ll):
    while ll:
        print(ll.val)
        ll = ll.next


def createll(lst):
    begin = None
    cur = None
    for item in lst:
        node = ListNode(item, None)
        if cur:
            cur.next = node
            cur = cur.next
        else:
            begin = node
            cur = begin

    return begin


l1ptr = createll([2,4,3])
l2ptr = createll([5,6,4])

sol = Solution()


l3ptr = sol.addTwoNumbers(l1ptr,l2ptr)

printll(l3ptr)


l1ptr = createll([9,9,9,9,9,9,9])
l2ptr = createll([9,9,9,9])

l3ptr = sol.addTwoNumbers(l1ptr,l2ptr)

printll(l3ptr)
