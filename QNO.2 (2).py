def largestElement(arr):
    max_val = arr[0]      
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

arr = [10, 20, 4, 45, 99]
print("Largest element:", largestElement(arr))
