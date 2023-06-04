def kadane_algorithm(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum += arr[i]
        if current_sum < arr[i]:
            current_sum = arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray_sum = kadane_algorithm(arr)
print(max_subarray_sum)
