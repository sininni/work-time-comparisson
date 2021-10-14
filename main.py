import json
from array_generation import *
from time import time
import pprint
from copy import deepcopy
from help_fun import *

array_dict = {0: new_lst_create(),    # random list
              1: new_lst_create(),    # increse
              2: new_lst_create(),    # decrease
              3: new_lst_create()}    # set

last_index = 0

def help_function(number_of_lst: int, num_of_repeats: int):

    for k in range(4):
        array_dict[number_of_lst][k][0].insert(last_index, 0)
        array_dict[number_of_lst][k][1].insert(last_index, 0)

    for i in range(num_of_repeats):
        lst = a.lst_generator(number_of_lst)

        for l in range(4):

            start = time()
            array_dict[number_of_lst][l][1].insert(last_index, array_dict[number_of_lst][l][1][last_index] + \
                                                   (sort_call(l, deepcopy(lst)) // num_of_repeats))

            array_dict[number_of_lst][l][0].insert(last_index, array_dict[number_of_lst][l][0][last_index] + \
                                                  (time() - start) / num_of_repeats)

            array_dict[number_of_lst][l][1].pop()
            array_dict[number_of_lst][l][0].pop()


for i in range(7, 16):
    a = ArrayGeneration(i)

    for k in range(4):

        ran_time_average = 0
        ran_operation_num = 0
        if k == 0:
            help_function(k, 5)

        elif k == 3:
            help_function(k, 3)

        else:
            help_function(k, 1)

    last_index += 1
    print(f"{i}th search was ended")

with open('result.json', 'w') as fp:
    json.dump(array_dict, fp)
