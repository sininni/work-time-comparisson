from typing import List


def selection_sort(lst: List[int]) -> int:
    count_comp = 0

    for i in range(len(lst)):

        # find min item in unsorted part of list
        min_idx = i
        for j in range(i + 1, len(lst)):
            count_comp += 1
            if lst[min_idx] > lst[j]:
                min_idx = j

        # swap min item of unsorted part with 1st item of unsorted part
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    #print(lst)
    return count_comp

