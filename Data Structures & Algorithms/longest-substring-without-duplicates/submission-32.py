class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        current = set()
        maxLength = 0 
        left = 0

        for right in range(len(s)):

            while s[right] in current: 
                current.remove(s[left])
                left += 1
            
            current.add(s[right])

            maxLength = max(maxLength, (right - left + 1))

        return maxLength