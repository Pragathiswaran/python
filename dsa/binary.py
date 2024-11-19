# Binary search algorithm in 1D array
def binary(nums, key):
    left, right = 0, len(nums) - 1
    mid = (left + right) // 2

    while left < right:
        if nums[mid] == key:
            return 'Found in position {}'.format(mid)
        elif nums[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    return 'Not found'


# res = binary([-1, 0, 3, 5, 9, 12], 13)
# print(res)


# print((0 + 5) // 2)
# 2D Array
def searchMatrix(matrix, target):
    left, mid, right = 0, 0, 0
    for num in matrix:
        if num[0] <= target and num[-1] >= target:
            right = len(num) - 1
            mid = (left + right) // 2

            while left <= right:
                if num[mid] == target:
                    return True
                elif num[mid] < target:
                    left = mid + 1
                else:
                    right = mid + 1
                mid = (left + right) // 2

        left, mid, right = 0, 0, 0

    return False


max = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# value = searchMatrix(max, 3)
# print(value)
# print(len(max))
# print(divmod(11, 4))


def searchMatrix_(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        # Convert mid index to 2D indices
        row, col = divmod(mid, cols)
        print(row, col)
        mid_value = matrix[row][col]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
            print('left', left)
        else:
            right = mid - 1
            print('right', right)

    return False


# value = searchMatrix_(max, 3)
# print(value)

# print(3|1)

print(3//2)
print(11 < 3)
print(divmod(1, 4))
