###################### Heap Method ###################

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


################ Quick Select Method ################################


def partition(arr, lo, hi):
    i, j = lo - 1, lo
    pivot = arr[hi]
    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    
    return i
    
def quickSelect(arr, l, r, k):
    
    pivotIndex = partition(arr, l, r)
    if pivotIndex  < k:
        return quickSelect(arr, pivotIndex + 1, r, k)
    elif pivotIndex > k:
        return quickSelect(arr, l, pivotIndex - 1, k)
    else:
        return arr[pivotIndex]
    
def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    return quickSelect(arr, l, r, k-1)

                