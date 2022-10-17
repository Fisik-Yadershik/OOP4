#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Решите следующую задачу: напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
соединение, строк. В остальных случаях введенные числа суммируются.
"""


class Summ():
    def __init__(self, inp1, inp2):
        self.a = inp1
        self.b = inp2

    def summ(self):
        print("Сумма чисел: ", int(self.a) + int(self.b))

    def cont(self):
        print("Результат конкатенации: ", self.a + self.b)


def main():
    try:
        inp1 = input("Введите первое число: ")
        inp2 = input("Введите второе число: ")
        summ = Summ(inp1, inp2)
        summ.summ()
    except ValueError as v:
        summ = Summ(inp1, inp2)
        summ.cont()


if __name__ == "__main__":
    main()