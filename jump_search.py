# searches sorted array for a number using jump search | runtime: O(sqrt(n))
import math

array = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 14, 15, 19, 21, 23, 30, 32, 35]


def jump_search(arr, num):
    length = len(arr)

    block = round(math.sqrt(length))
    iterations = 0

    block_searching = True

    while block_searching:
        if block * iterations >= length:
            print("not found")
            return False
        else:
            lower = arr[block * iterations]

        if block * (iterations + 1) >= length:
            upper = arr[length - 1]
        else:
            upper = arr[block * (iterations + 1)]

        if lower <= num <= upper:
            block_searching = False
            break
        else:
            iterations += 1

    for i in arr[block * iterations: block * (iterations + 1)]:
        if i == num:
            print("found")
            return True

    print("not found")
    return False


jump_search(array, 23)
