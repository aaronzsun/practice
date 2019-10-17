# searches sorted array for a number using binary search | runtime: O(log n)
array = [1, 2, 3, 5, 6, 7, 8, 9, 10]


def bi_search(arr, num):
    if len(arr) > 1:
        length = len(arr)
        mid = round(length / 2)
        mid_num = arr[mid]
        if num == mid_num:
            print("found")
            return True
        elif num < mid_num:
            bi_search(arr[:mid], num)
        elif num > mid_num:
            bi_search(arr[mid:], num)
    else:
        print("not found")
        return False


bi_search(array, 5)
