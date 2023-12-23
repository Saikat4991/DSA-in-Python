class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if length of s1 is biggere then it not possible to substring of s2
        if len(s1) > len(s2):
            return False
        
        cntr = Counter(s1)
        l = len(s1)
        
        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
            
            if i>=l and s2[i-l] in cntr:
                cntr[s2[i-l]] += 1
                
            if all([cntr[j] == 0 for j in cntr]):
                return True
            
        return False

        
        