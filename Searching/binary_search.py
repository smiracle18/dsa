def binary_search(arr, target):
    ''' input: sorted arr and returns the occurance of target in it.
        output: index of target in arr starting from 0.
    '''
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))