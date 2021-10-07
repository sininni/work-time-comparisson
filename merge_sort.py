# Python program for implementation of MergeSort
from typing import List

def merge_sort(lst: List[int]) -> int:

    # count len(lst) > 1 last comparisson if len == 0
    count_comp = 1
    if len(lst) > 1:
        count_comp += 1

        # find the middle of the list
        mid = len(lst) // 2

        # divide list into two halfs
        left = lst[:mid]
        right = lst[mid:]

        # recursively sort each half
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        count_comp += 2

        while i < len(left) and j < len(right):
            count_comp += 2

            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
            count_comp += 1

        # ???
        count_comp += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
            count_comp += 1

        count_comp += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
            count_comp += 1

    return count_comp


