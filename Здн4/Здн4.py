#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import json
import pathlib
import logging
import logging.config


class FlightTable:
    def __init__(self, line):
        self.line = line
        
    def selecting(self, flights, nom):
        """Выбор рейсов по типу самолёта"""
        count = 0
        print(self.line)
        print(
            '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
                "№",
                "Место прибытия",
                "Номер самолёта",
                "Тип"))
        print(self.line)
        for i, num in enumerate(flights, 1):
            if nom == num.get('value', ''):
                count += 1
                print(
                    '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                        count,
                        num.get('stay', ''),
                        num.get('number', ''),
                        num.get('value', 0)))
        print(self.line)

    def table(self, flights):
        """Вывод скиска рейсов"""
        print(self.line)
        print(
            '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
                "№",
                "Место прибытия",
                "Номер самолёта",
                "Тип"))
        print(self.line)
        for i, num in enumerate(flights, 1):
            print(
                '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                    i,
                    num.get('stay', ''),
                    num.get('number', ''),
                    num.get('value', 0)
                )
            )
        print(self.line)

    def adding(self, flights, stay, number, value):
        flights.append(
            {
                'stay': stay,
                'number': number,
                'value': value
            }
        )
        return flights

    def saving(self, file_name, flights):
        with open(file_name, "w", encoding="utf-8") as file_out:
            json.dump(flights, file_out, ensure_ascii=False, indent=4)
        logging.info(f"Данные сохранены в файл: {file_name}")

    def opening(self, file_name):
        with open(file_name, "r", encoding="utf-8") as f_in:
            return json.load(f_in)


def main(command_line=None):

    logging.basicConfig(
            filename='flight.log',
            level=logging.INFO,
            format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s"
        )

    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 20,
        '-' * 15,
        '-' * 16
    )
    fl = FlightTable(line)

    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",)
    parser = argparse.ArgumentParser("flights")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0")
    subparsers = parser.add_subparsers(dest="command")
    add = subparsers.add_parser(
        "add",
        parents=[file_parser])
    add.add_argument(
        "-s",
        "--stay",
        action="store",
        required=True,)
    add.add_argument(
        "-v",
        "--value",
        action="store",
        required=True,)
    add.add_argument(
        "-n",
        "--number",
        action="store",
        required=True,)
    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],)
    select = subparsers.add_parser(
        "select",
        parents=[file_parser],)
    select.add_argument(
        "-t",
        "--type",
        action="store",
        required=True,)
    args = parser.parse_args(command_line)
    is_dirty = False
    name = args.filename
    home = pathlib.Path.cwd()/name

    try:
        flights = fl.opening(home)
        logging.info("Файл найден, продолжаем работы с данными полученного файла")
    except FileNotFoundError as e:
        flights = []
        logging.warning("Файл не был найден, создаётся новый.")

    if args.command == "add":
        flights = fl.adding(flights, args.stay, args.number, args.value)
        is_dirty = True
        logging.info("Добавлен рейс")
    elif args.command == 'display':
        fl.table(flights)
        logging.info("Отображён список рейсов")
    elif args.command == "select":
        fl.selecting(flights, args.type)
        logging.info("Выбраны рейсы по типу самолёта")

    if is_dirty:
        fl.saving(args.filename, flights)


if __name__ == '__main__':
    main()