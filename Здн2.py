#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
from pprint import pprint


"""
Решите следующую задачу: напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
соединение, строк. В остальных случаях введенные числа суммируются.
"""


class Matrix:
    def __init__(self, inp1, inp2, inp3, inp4):
        self.strok = int(inp1)
        self.stolb = int(inp2)
        self.min = int(inp3)
        self.max = int(inp4)

    def random_init(self):
        pprint([[random.randrange(self.min, self.max) for y in range(self.stolb)] for x in range(self.strok)])


def main():
    try:
        inp1 = input("Введите количетсво строк: ")
        inp2 = input("Введите количетсво столбцов: ")
        inp3 = input("Введите минимальную границу диапазона чисел: ")
        inp4 = input("Введите максимальную границу диапазона чисел: ")
        mat = Matrix(inp1, inp2, inp3, inp4)
        mat.random_init()
    except ValueError as v:
        print("Ошибка при вводе значения!")


if __name__ == "__main__":
    main()