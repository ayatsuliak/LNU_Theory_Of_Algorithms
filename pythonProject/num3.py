def count_unique(arr):
    unique_set = set()
    for el in arr:
        unique_set.add(el)
    return len(unique_set)


arr = [2, 4, 5, 2, 4, 5]

print(count_unique(arr))
