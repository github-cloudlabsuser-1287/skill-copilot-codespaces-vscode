# write a function that takes a list of integers and returns a sorted list using quick sort algorithm
# Example: [3, 2, 1, 5, 4] => [1, 2, 3, 4, 5]
#
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([3, 2, 1, 5, 4])) # [1, 2, 3, 4, 5]
print(quick_sort([1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]
print(quick_sort([5, 4, 3, 2, 1])) # [1, 2, 3, 4, 5]
print(quick_sort([1, 3, 2, 5, 4])) # [1, 2, 3, 4, 5]
print(quick_sort([1, 2, 3, 5, 4])) # [1, 2, 3, 4, 5]




