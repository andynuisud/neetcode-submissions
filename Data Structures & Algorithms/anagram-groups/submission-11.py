class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for i in range(len(strs)):
            sortedString = "".join(sorted(strs[i]))
            hashMap[sortedString].append(strs[i])

        return list(hashMap.values())