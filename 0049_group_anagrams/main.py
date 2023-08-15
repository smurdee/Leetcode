class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        for i, e in enumerate(strs):
            sorted_str = ''.join(sorted(e))
            if sorted_str in sorted_words:
                sorted_words[sorted_str].append(e)
            else:
                sorted_words[sorted_str] = [e]
        return sorted_words.values()