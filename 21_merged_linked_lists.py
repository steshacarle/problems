# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1


        if list1.val < list2.val:
            newNode = ListNode(list1.val)
            newNode.next = self.mergeTwoLists(list1.next, list2)
        else:
            newNode = ListNode(list2.val)
            newNode.next = self.mergeTwoLists(list1, list2.next)

        return newNode

# [1, 2, 4]
# [2, 3, 4]
'''
mergeTwoLists ->
  list1 = [1,2,4]
  list2 = [2,3,4]

call 1:
  newNode = {val: 1, next: None}
  newNode = {val: 1, next: result of call 2}

call 2:
  list 1 = [2,4]
  list 2 = [2,3,4]
  newNode = {val: 2, next: result of call 3}

call 3:
  list 1 = [2,4]
  list 2 = [3,4]
  newNode = {val: 2, next: result of call 4}

call 4:
  list 1 = [4]
  list 2 = [3,4]
  newNode = {val: 3, next: result of call 5}

call 5:
  list 1 = [4]
  list 2 = [4]
  newNode = {val: 4, next: result of call 6}

call 6:
  list 1 = [4]
  list 2 = None
  {val: 4, next: None} ---->

result of call 6: {val: 4, next: None}

result of call 5: {val: 4, next: {val: 4, next: None}}

result of call 4: {val: 3, next: {val: 4, next: {val: 4, next: None}}}

result of call 3: {val: 2, next: {val: 3, next: {val: 4, next: {val: 4, next: None}}}}

result of call 2: {val: 2, next: {val: 2, {val: 3, next: {val: 4, next: {val: 4, next: None}}}}}

result of call 1: {val: 1, next: {val: 2, next: {val: 2, {val: 3, next: {val: 4, next: {val: 4, next: None}}}}}}
'''
