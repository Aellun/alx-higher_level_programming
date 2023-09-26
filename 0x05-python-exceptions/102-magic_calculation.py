#!/usr/bin/python3


def magic_calculation(a, b):
    cal_result = 0
    for item in range(1, 3):
        try:
            if item > a:
                raise Exception('Too far')
            else:
                cal_result += a ** b / item
        except ValueError:
            cal_result = b + a
            break
    return (cal_result)
