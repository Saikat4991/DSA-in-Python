class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s)==Counter(t) using python inbuilt function
        # return sorted(s)==sorted(t) using sorting time= O(nlogn) space=O(1)
        if len(s)!=len(t):
            return False

        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
