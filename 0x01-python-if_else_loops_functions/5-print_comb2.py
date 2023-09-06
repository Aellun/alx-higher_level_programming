#!/usr/bin/python3
"""Print numbers from 0 to 98 in both decimal and hexadecimal."""
for num in range(0, 100):
    if num == 99:
        print("{:02}".format(num))
    else:
        print("{:02}".format(num), end=", ")
