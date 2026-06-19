class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashSet1 = defaultdict(int)
        hashSet2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hashSet1[s[i]] += 1
            hashSet2[t[i]] += 1

        return hashSet1 == hashSet2
        