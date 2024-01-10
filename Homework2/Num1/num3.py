def func(arr, x):
    i, j = 0, 0
    while i < len(arr[0]) or j < len(arr[1]):
        if arr[0][i] == x or arr[1][j] == x:
            return True
        else:
            i += 1
            j += 1
    return False


arr = [[2, 4, 1, 6, 7], [2, 7, 8, 12, 4]]
print(func(arr, 4))
