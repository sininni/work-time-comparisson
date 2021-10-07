from typing import List


def insertion_sort(lst: List[int]) -> int:
    count_comp = 0
    for i in range(1, len(lst)):

        key = lst[i]

        # move items of array greater than key to one position ahead
        j = i - 1
        count_comp += 2
        while j >= 0 and key < lst[j]:
            count_comp += 2
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    return count_comp

