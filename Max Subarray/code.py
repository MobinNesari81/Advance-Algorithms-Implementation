def max_subarray(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2

    left_sum = max_subarray(arr[:mid])
    right_sum = max_subarray(arr[mid:])
    cross_sum = max_crossing_subarray(arr, mid)

    return max(left_sum, right_sum, cross_sum)

def max_crossing_subarray(arr, mid):
    left_sum = float('-inf')
    curr_sum = 0

    for i in range(mid - 1, -1, -1):
        curr_sum += arr[i]
        left_sum = max(left_sum, curr_sum)

    right_sum = float('-inf')
    curr_sum = 0

    for i in range(mid, len(arr)):
        curr_sum += arr[i]
        right_sum = max(right_sum, curr_sum)

    return left_sum + right_sum

