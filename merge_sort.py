# merge sort algorithm | runtime: O(n log n)
array = [7, 3, 2, 5, 4, 9, 12, 11, 19, 2, 4, 5]


def merge_sort(arr):
    size = len(arr)
    if size > 1:
        mid = round(size / 2)
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


merge_sort(array)

print("Sorted Array:")
for element in array:
    print(element)
