class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        # count of most frequently occuring character in the window
        max_window_len = 0
        # left pointer
        l = 0

        def get_max(d):
            return max(i for i in d.values())

        for r, char in enumerate(s):
            window_len = r - l + 1
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

            while window_len - get_max(counts) > k:
                counts[s[l]] -= 1
                l += 1
                window_len = r - l + 1
            max_window_len = max(max_window_len, window_len)
        
        return max_window_len