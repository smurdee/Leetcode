import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = re.sub(r'[\W_]', '', s)
        # l = len(new_s)
        for i, e in enumerate(new_s):
            j = -i - 1
            if e != new_s[j]:
                return False
        return True