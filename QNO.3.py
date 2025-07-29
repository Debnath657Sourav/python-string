def second_largest(arr):
    if len(arr) < 2:
        return -1

    largest = second_largest_val = -1

    for num in arr:
        if num > largest:
            second_largest_val = largest
            largest = num
        elif num != largest and num > second_largest_val:
            second_largest_val = num

    return second_largest_val if second_largest_val != -1 else -1

arr = [10, 20, 4, 45, 99]
print("Second largest element:", second_largest(arr))
