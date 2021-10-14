from typing import List

# def shell_sort(lst: List[int]) -> int:
#     counter = 0
#     h = 1
#     while h < len(lst) // 2:
#         h = 3 * h + 1
#
#     while h >= 1:
#         for i in range(h, len(lst)):
#             j = i
#             counter += 1
#             for j in range(i, h, -h):
#
#                 if lst[j] < lst[j-h]:
#                     lst[j], lst[j-h] = lst[j-h], lst[j]
#
#         h = h // 2
#     return counter

def shell_sort(lst):
    n = len(lst)
    gap = int(n / 2)
    count_comp = 1

    while gap > 0:
        count_comp += 1

        for i in range(gap, n):

            temp = lst[i]
            j = i

            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            count_comp += 1
            lst[j] = temp
        gap //= 2

    return count_comp
