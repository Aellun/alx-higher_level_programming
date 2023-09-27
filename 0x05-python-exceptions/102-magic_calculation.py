#!/usr/bin/python3


import dis


def magic_calculation(a, b):
    cal_result = 0
    for item in range(1, a + 1):
        try:
            if item > a:
                raise Exception('Too far')
            else:
                cal_result += a ** b / item
        except ZeroDivisionError:
            return "Division by zero"
    return cal_result
