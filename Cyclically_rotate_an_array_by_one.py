def reverse(arr, left, right):
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
def rotate( arr, n):
    reverse(arr, 0, n-2)
    reverse(arr, 0, n-1)
    
    
