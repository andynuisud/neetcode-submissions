class Solution:
    def isValid(self, s: str) -> bool:
        
        hashMap = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []

        for i in range(len(s)):

            if s[i] in hashMap: 
                if not stack or stack.pop() != hashMap[s[i]]:
                    return False
            else: 
                stack.append(s[i])

        if stack: 
            return False
        return True 