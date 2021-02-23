"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    low = 0
    hiest = len(array)

    sorted_array = quick_sort(array)

    return sorted_array


def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array.pop()
    left_array = []
    right_array = []

    for n in array:
        if pivot > n:
            left_array.append(n)
        else:
            right_array.append(n)
    return quicksort(left_array)+[pivot]+quicksort(right_array)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
