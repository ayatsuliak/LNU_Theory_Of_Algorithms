# def find_smallest_number(a, b, c):
#     start_point = 0
#     set_a = set(a)
#     set_b = set(b)
#     set_c = set(c)
#     min_size = min(len(set_a), len(set_b), len(set_c))
#
#     for i in range(min_size):
#         min_value = min(a[start_point], b[start_point], c[start_point])
#         if min_value in set_a & set_b & set_c:
#             return min_value
#         start_point += 1
#
#     return None


def find_smallest_number(a, b, c):
    smallest_number = float('inf')
    for num in a + b + c:
        if num < smallest_number and num in a and num in b and num in c:
            smallest_number = num
    if smallest_number != float('inf'):
        return smallest_number
    else:
        return None


A = [1, 2]
B = [2, 3]
C = [1, 2, 3]

print(find_smallest_number(A, B, C))
