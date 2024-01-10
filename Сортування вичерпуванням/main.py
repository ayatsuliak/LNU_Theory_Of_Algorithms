def brute_force_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [2, 6, 4, 1, 7, 4, 9, 3]

print(brute_force_sort(arr))
