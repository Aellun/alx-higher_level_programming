#!/usr/bin/python3
# Loop through the ASCII values of lowercase letters
for Alpha in range(97, 123):
    # Check if the letter is not 'q' or 'e' and print it without a newline
    if chr(Alpha) != 'q' and chr(Alpha) != 'e':
        print(f"{chr(Alpha)}", end='')

