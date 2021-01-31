import heapq as hq
class Solution:
    def kthLargest(self, arr, k):
        '''
        :type arr: list of int
        :type k: int
        :rtype: int
        '''
        l = []
        hq.heapify(l)
    
        for i in range(0, k):
            hq.heappush(l, arr[i])
    
        for i in range(k, len(arr)):
            top = hq.heappop(l)
    
            if arr[i] < top:
                hq.heappush(l, top)
            else:
                hq.heappush(l, arr[i])
    
    
        return hq.heappop(l)
            
                