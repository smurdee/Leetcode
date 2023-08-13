class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1 = None, l2 = None):
        self.l1 = l1
        self.l2 = l2
        final_output = ListNode()

        buffer = final_output

        while ((l1!= None)|(l2!= None)):
            if (l1 == None):
                buffer.val += l2.val
                l2 = l2.next
            elif (l2 == None):
                buffer.val += l1.val
                l1 = l1.next
            else:
                buffer.val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next

            if buffer.val >= 10:
                buffer.val -= 10
                next_node = ListNode(1)
                buffer.next = next_node
                buffer = next_node
            else:
                if ((l1 != None) | (l2 != None)):
                    next_node = ListNode(0)
                    buffer.next = next_node
                    buffer = next_node

        return final_output


## DEBUG ONLY

# def ListCreator(l1 = list, l2 = list):
#     out1 = ListNode(l1[0])
#     buffer = out1
#     if len(l1) > 1:
#         for i in range(1, len(l1)):
#             next1 = ListNode()
#             buffer.next = next1
#             buffer = next1
#             buffer.val = l1[i]

#     out2 = ListNode(l2[0])
#     buffer = out2
#     if len(l2) > 1:
#         for i in range(1, len(l2)):
#             next2 = ListNode()
#             buffer.next = next2
#             buffer = next2
#             buffer.val = l2[i]

#     return out1, out2

# input1, input2 = ListCreator([9,9,9,9,9,9,9], [9,9,9,9])

# answer = Solution()
# test = answer.addTwoNumbers(input1, input2)

# while test != None:
#     print(test.val)
#     test = test.next