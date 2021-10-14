# class, whcih generates different number arrays
from random import randint


class ArrayGeneration():

    def __init__(self, power):
        self.power = power
        self.size = 2 ** self.power

    def random_lst(self):
        random_lst = [randint(1, self.size) for _ in range(self.size)]
        return random_lst

    def increase_lst(self):
        random_lst = [x for x in range(self.size)]
        return random_lst

    def decrease_lst(self):
        random_lst = [(self.size - i) for i in range(self.size)]
        return random_lst

    def set_lst(self):
        random_lst = [randint(1, 3) for _ in range(self.size)]
        return random_lst

    def lst_generator(self, num: int):
        if num == 0:
            return self.random_lst()
        elif num == 1:
            return self.increase_lst()
        elif num == 2:
            return self.decrease_lst()
        else:
            return self.set_lst()
