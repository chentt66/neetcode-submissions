class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # sorted word: each word
        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups.keys():
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())