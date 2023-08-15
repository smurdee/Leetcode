class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        node_dictionary = {}
        longest = 0
        for e in nums:
            if e not in node_dictionary:
                node_dictionary[e] = Element(e)
                if (e-1 in node_dictionary) and (e+1 in node_dictionary):
                    node_dictionary[e-1].left.right = node_dictionary[e+1].right
                    node_dictionary[e+1].right.left = node_dictionary[e-1].left
                    node_dictionary[e].left = node_dictionary[e-1].left
                    node_dictionary[e].right = node_dictionary[e+1].right
                elif e-1 in node_dictionary:
                    node_dictionary[e].left = node_dictionary[e-1].left
                    node_dictionary[e-1].left.right = node_dictionary[e]
                elif e+1 in node_dictionary:
                    node_dictionary[e+1].right.left = node_dictionary[e]
                    node_dictionary[e].right = node_dictionary[e+1].right

                longest = max(longest, node_dictionary[e].get_length())

        return longest

class Element:
    def __init__(self, value):
        self.value = value
        self.left = self
        self.right = self
    
    def get_length(self):
        return self.right.value - self.left.value + 1