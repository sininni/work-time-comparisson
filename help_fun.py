from typing import List
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from shell_sort import shell_sort


def new_lst_create():
    lst = []
    for _ in range(4):
        lst.append([[], []])
    return lst

def sort_call(num: int, lst: List[int]) -> int:
    if num == 0:
        return insertion_sort(lst)
    elif num == 1:
        return merge_sort(lst)
    elif num == 2:
        return selection_sort(lst)
    else:
        return shell_sort(lst)
