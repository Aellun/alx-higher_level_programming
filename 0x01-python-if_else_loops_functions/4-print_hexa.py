#!/usr/bin/python3
"""Prints num both in decimal and hexadecimal ranging 0 to 98."""
for num in range(0, 99):
    print("{} = {}".format(num, hex(num)))
