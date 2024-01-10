def merge_arrays(a, b):
    m, n = len(a), len(b)
    c = [0] * (m + n)
    i, j, k = 0, 0, 0

    while i < m and j < n:
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1

    while i < m:
        c[k] = a[i]
        i += 1
        k += 1

    while j < n:
        c[k] = b[j]
        j += 1
        k += 1

    return c


A = [1, 1, 2, 3, 3]
B = [2, 2, 3, 4]

print(merge_arrays(A, B))
