def binary_search_recursive(arr: list, left: int, right: int, target: int) -> int:
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid # location of the item in the array
        elif arr[mid] < target:
            return binary_search_recursive(arr, mid+1, right, target)
        else:
            return binary_search_recursive(arr, left, mid -1, target)
    else:
        return None


def binary_search_iterative(arr: list, target:int) -> int:
    left = 0
    right = len(arr) - 1
    mid = left

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search_recursive(data, 0, len(data) - 1, 5))
print(binary_search_recursive(data, 0, len(data) - 1, 10))
print(binary_search_recursive(data, 0, len(data) - 1, 15))
print(binary_search_iterative(data,  5))
print(binary_search_iterative(data,  10))
print(binary_search_iterative(data,  15))
'''
O(log n) time complexity 
O(log n) space complexity
'''