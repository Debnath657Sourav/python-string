def rotate_by_one(arr):
    if len(arr) <= 1:
        return arr

    last = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last
    return arr


arr = [1, 2, 3, 4, 5]
rotated = rotate_by_one(arr)
print(rotated) 
