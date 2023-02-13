"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""


import sys
from sys import argv

f_obj, name_v, rate_v,hours_v = sys.argv
def calculate_salary(rate, hours):
    try:
        print(f"Сотрудник {name_v} заработал {int(rate) * int(hours) * 1.25}")
    except TypeError:
        print("Операция применена к объекту несоответствующего типа")
        exit()

calculate_salary(rate_v, hours_v)