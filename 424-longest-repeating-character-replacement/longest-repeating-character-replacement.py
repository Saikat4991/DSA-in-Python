class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #initialize
        left = 0 # left : start index of sliding windows
        countChar = {} # Dict to store count of each charecter
        maxFreq = 0 # max frequency of each charecter in the sub window
        maxLen = 0 # Maximum count of any single character in the substring


        for right in range(len(s)): # right: end idx of sliding windows
            # update count of each char
            countChar[s[right]] = 1 + countChar.get(s[right],0)

            # Update the maximum count of any single character in the substring
            maxFreq = max(maxFreq, countChar[s[right]])

            if (right - left + 1) - maxFreq > k:
                # reduce countChar by 1 and shift left by 1
                countChar[s[left]] -= 1
                left += 1

            # Update the maximum length of the repeating substring
            maxLen = max(maxLen, right - left + 1)

        return maxLen

















            
        

        