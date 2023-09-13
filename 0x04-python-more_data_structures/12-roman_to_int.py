#!/usr/bin/python3


"""function: def roman_to_int(roman_string) converts Roman numeral to int
    assume the number will be between 1 to 3999.
    return: 0 if none or roman_string is not a string"""


def to_subtract(num_list):
    sub_to = 0
    max_list = max(num_list)

    for n in num_list:
        if max_list > n:
            sub_to += n

    return (max_list - sub_to)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    num_list = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(num_list)
                    num_list = [rom_n.get(ch)]
                else:
                    num_list.append(rom_n.get(ch))

                last_rom = rom_n.get(ch)

    num += to_subtract(num_list)

    return (num)
