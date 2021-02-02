def sort012(arr,n):
    left, mid, right = 0, 0, n-1
    
    while mid <= right:
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
            
        else: mid += 1
        

