#!/usr/bin/python3
def roman_to_int(roman_string):
    sum_rom = []
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum_rom_copy = []

    if roman_string is None or type(roman_string) != str:
        return 0
    for i in roman_string:
        if i in rom_dic.keys():
            sum_rom.append(rom_dic.get(i))

    sum_rom.append(0)
    for x, y in zip(sum_rom[::1], sum_rom[1::1]):
        if y > x:
            x *= -1
        sum_rom_copy.append(x)
        if len(sum_rom) < 3:
            sum_rom_copy.append(y)
    number = sum(sum_rom_copy)
    return number
