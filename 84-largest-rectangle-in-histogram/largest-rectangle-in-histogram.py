class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # Previous Smaller Index
        def prevSmallerInx(x):
            n = len(x)
            stk = []
            prevIdx = [0]*n
            for i in range(n):
                while len(stk) !=0 and x[stk[-1]] >= x[i]:
                    stk.pop()
                
                if len(stk) == 0:
                    prevIdx[i] = -1
                else:
                    prevIdx[i] = stk[-1]
                
                stk.append(i)

            return prevIdx

        # Next Smaller Index
        def nxtSmallerIdx(x):
            n = len(x)
            stk = []
            nxtIdx = [0]*n
            for i in range(n):
                while len(stk) != 0 and x[n-i-1] <= x[stk[-1]]:
                    stk.pop()
                if len(stk) ==0:
                    nxtIdx[n-i-1] = n
                else:
                    nxtIdx[n-i-1] = stk[-1]

                stk.append(n-i-1)
            return nxtIdx

        maxArea = 0
        prevSIdx = prevSmallerInx(heights)
        nxtSIdx = nxtSmallerIdx(heights)
        for i in range(len(heights)):
            area = heights[i]*(nxtSIdx[i] - prevSIdx[i] - 1)
            maxArea = max(area, maxArea)
        return maxArea

 
                
                
                
                
                

                    


        