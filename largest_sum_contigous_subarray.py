class Solution:
    def maxSubArray(self, A):
        currMax, totalMax = A[0], A[0]
        endIndex = 0
        for i in range(1, len(A)):
            currMax = max(A[i], currMax + A[i])
            if currMax > totalMax:
                totalMax = currMax
                endIndex = i
        startIndex, tempMax = endIndex, totalMax
        
        while startIndex >= 0:
            if tempMax == 0: break
            tempMax -= A[startIndex]
            startIndex -= 1
        print(startIndex, endIndex)
        return totalMax
