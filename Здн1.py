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
        if (self.a.isnumeric()==True) and (self.b.isnumeric==True):
            print("Сумма чисел: ", int(self.a) + int(self.b))
        else:
            print("Результат конкатенации: ", self.a + self.b)

    def cont(self):
        print("Результат конкатенации: ", self.a + self.b)


def main():
    inp1 = input("Введите первое число: ")
    inp2 = input("Введите второе число: ")
    summ = Summ(inp1, inp2)
    summ.summ()

if __name__ == "__main__":
    main()