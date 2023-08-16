class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == '{':
                stack.append(i)
            elif i == '[':
                stack.append(i)
            elif len(stack) < 1:
                return False
            elif i == ')' and stack.pop() != '(':
                return False
            elif i == '}' and stack.pop() != '{':
                return False
            elif i == ']' and stack.pop() != '[':
                return False
        
        return not stack