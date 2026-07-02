class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        left = 0
        right = len(s)-1
        max_window = 0
        sub = set()

        for right in range(len(s)):

            while s[right] in sub:
                sub.remove(s[left])
                left +=1
            
            sub.add(s[right])
            max_window = max(max_window,right-left+1)

        return max_window