def merge_sort(array):
    size = len(array)

    if size <= 1:
        return array

    midpoint = int(size / 2)
    left_array, right_array = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left_array, right_array)


# My Method_______________
# def merge(left_array, right_array):
#     sorted_array = []
#
#     while len(left_array) > 0 and len(right_array) > 0:
#
#         if left_array[0] < right_array[0]:
#             sorted_array.append(left_array.pop(0))
#         else:
#             sorted_array.append(right_array.pop(0))
#
#     if len(left_array) > 0:
#         sorted_array.extend(left_array)
#     else:
#         sorted_array.extend(right_array)
#
#     return sorted_array

# Youtube Method:
def merge(left_array, right_array):
    sorted_array = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left_array) and right_pointer < len(right_array):

        if left_array[left_pointer] < right_array[right_pointer]:
            sorted_array.append(left_array[left_pointer])
            left_pointer += 1
        else:
            sorted_array.append(right_array[right_pointer])
            right_pointer += 1

    sorted_array.extend(left_array[left_pointer:])
    sorted_array.extend(right_array[right_pointer:])

    return sorted_array


def main():
    array = [25, 12, 18, 42, 9, 4, 71, 85, 19, 14, 11, 12, 17, 29, 44, 45, 1, 33, 37, 18, 14, 28]
    print(array)
    print(merge_sort(array))


if __name__ == "__main__":
    main()
