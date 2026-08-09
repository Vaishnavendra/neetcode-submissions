class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        emtmap=defaultdict(list)
        for char in strs:
            count=[0]*26
            for c in char:
                count[ord(c)-ord('a')] += 1
            emtmap[tuple(count)].append(char)
        return list(emtmap.values())