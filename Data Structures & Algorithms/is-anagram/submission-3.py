class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashMap1 = defaultdict(int)
        hashMap2 = defaultdict(int)
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hashMap1[s[i]] += 1
            hashMap2[t[i]] += 1


        return (hashMap1 == hashMap2)