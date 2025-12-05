def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2   # middle index

        if arr[mid] == target:
            return mid              # found it!
        elif arr[mid] < target:
            left = mid + 1          # search right half
        else:
            right = mid - 1         # search left half

    return -1   # not found

print(binary_search([1,2,3,4,5] , 5))

# [f, f, f, t ,t ]
