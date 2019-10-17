# searches an array for a number using linear search | runtime: O(n)
array = [7, 3, 2, 5, 4, 9, 12]


def li_search(arr, num):
    for i in arr:
        if i == num:
            print("found")
            return True
    print("not found")
    return False


li_search(array, 4)
